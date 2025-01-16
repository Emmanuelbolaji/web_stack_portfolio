from django.contrib.auth.models import User
from django.db import models
from item.models import Item

class Conversation(models.Model):
    """
    Model representing a conversation between users about an item.

    A conversation is associated with a specific item and can have multiple members
    (users) participating in it.

    Attributes:
        item (ForeignKey): The item being discussed
        members (ManyToManyField): Users participating in the conversation
        created_at (DateTimeField): When the conversation was created
        modified_at (DateTimeField): When the conversation was last modified
                                        
    Meta:
        ordering: Orders conversations by most recently modified first
    """
    item = models.ForeignKey(Item, related_name='conversation', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

class ConversationMessage(models.Model):
    """
    Model representing a single message within a conversation.

    Each message belongs to a conversation, has content, and is associated with
    the user who created it.

    Attributes:
        conversation (ForeignKey): The conversation this message belongs to
        content (TextField): The actual message content
        created_at (DateTimeField): When the message was created
        created_by (ForeignKey): The user who created the message
    """
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
