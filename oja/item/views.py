
m django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import NewItemForm, EditItemForm
from .models import Category, Item

def items(request):
    """
    Display list of items with optional filtering by category and search query.

       Handles the main item listing page with support for:
        - Filtering by category
        - Text search across name and description 
        - Excluding sold items
        - Excluding authenticated user's own items

    Args:
        request: HTTP request object with optional query parameters
            'query' for search text and 'category' for category filtering

    Returns:
         Rendered template with filtered items and filter parameters
    """
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()

    items = Item.objects.filter(is_sold=False)

    if request.user.is_authenticated:
        items = items.exclude(created_by=request.user)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query)
                )

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
        })

    def detail(request, pk):
        """
        Display detailed view of a specific item with related items.

        Shows full item details and related items from the same category.
        Related items behavior changes based on:
        - Whether user is authenticated
        - Whether accessed from dashboard
                       
        Args:
            request: HTTP request object
            pk (int): Primary key of the item to display

        Returns:
            Rendered template with item details and related items

        Raises:
            Http404: If item with given pk doesn't exist
        """
        item = get_object_or_404(Item, pk=pk)
        referer = request.META.get('HTTP_REFERER', '')

        related_query = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)

        if 'dashboard' in referer and request.user.is_authenticated:
            related_items = related_query.filter(created_by=request.user)[:3]
        elif request.user.is_authenticated:
            related_items = related_query.exclude(created_by=request.user)[:3]
        else:
            related_items = related_query[:3]

        return render(request, 'item/detail.html', {
            'item': item,
            'related_items': related_items
            })

@login_required
def new(request):
    """
    Create a new item listing.

    Handles both GET (show form) and POST (process form) requests.
    Requires user authentication.

    Args:
        request: HTTP request object with possible POST data and files

    Returns:
        On GET: Rendered form template
        On successful POST: Redirect to item detail
        On invalid POST: Rendered form template with errors
    """
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)

@login_required
def delete(request, pk):
    """
    Delete an item listing.

    Only allows deletion of items created by the requesting user.
    Requires user authentication.

    Args:
        request: HTTP request object with possible POST data and files
        pk (int): Primary key of the item to edit

    Returns:
        On GET: Rendered form template with existing item data
        On successful POST: Redirect to item detail
        On invalid POST: Rendered form template with errors

    Raises:
        Http404: If item doesn't exist or wasn't created by requesting user
    """
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
        })
