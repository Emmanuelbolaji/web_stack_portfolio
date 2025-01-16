from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, item_pk):
    """
    Create a new conversation for an item between a buyer and seller.
       
    This view handles the creation of new conversations and initial messages.
    If a conversation already exists between these users for this item,
    redirects to that conversation instead of creating a new one.
                   
    Args:
        request (HttpRequest): The HTTP request object
        item_pk (int): Primary key of the item being discussed

    Returns:
        HttpResponse: 
            - Redirect to dashboard if user is item owner
            - Redirect to existing conversation if one exists
            - Redirect to item detail on successful creation
            - Rendered form for new conversation otherwise
    Raises:
        Http404: If the item doesn't exist
    """
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item, members=request.user)

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
        else:
            form = ConversationMessageForm()
        return render(request, 'conversation/new.html', {
            'form': form'form': form
            })

@login_required
def inbox(request):
    """
    Display all conversations for the current user.

    Args:
        request (HttpRequest): The HTTP request object
    
    Returns:
        HttpResponse: Rendered inbox template with user's conversations

    Context:
        conversations (QuerySet): All conversations where user is a member
    """
    conversations = Conversation.objects.filter(members=request.user)

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
        })


@login_required
def detail(request, pk):
    """
    Display a specific conversation and handle new message creation.
       
    Shows the conversation history and provides a form for adding new messages.
    Updates the conversation's modified timestamp when new messages are added.
                
    Args:
        request (HttpRequest): The HTTP request object
        pk (int): Primary key of the conversation to display

    Returns:
        HttpResponse: 
            - Redirect back to conversation on successful message creation
            - Rendered conversation detail template otherwise
    Context:
        conversation (Conversation): The requested conversation object
        form (ConversationMessageForm): Form for adding new messages
    """
    conversation = Conversation.objects.filter(members=request.user).get(pk=pk)

    form = ConversationMessageForm()

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
                                                        
            conversation.save()
                                                                              
            return redirect('conversation:detail', pk=pk)

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
        })

