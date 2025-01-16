ngo.contrib import admin
from .models import Conversation, ConversationMessage

"""
Admin configuration for the conversation app.

Registers the Conversation and ConversationMessage models with the Django admin interface
for basic CRUD operations.
"""

admin.site.register(Conversation)
admin.site.register(ConversationMessage)
