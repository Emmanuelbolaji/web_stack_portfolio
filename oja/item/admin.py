from django.contrib import admin
from .models import Category, Item

"""
Admin configuration for the item app.

Registers the Category and Item models with the Django admin interface
for management through the admin panel.
"""

admin.site.register(Category)
admin.site.register(Item)
