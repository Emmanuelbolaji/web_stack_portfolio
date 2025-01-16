from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item

@login_required
def index(request):
    """
    Renders the dashboard page for the logged-in user.

    This view retrieves all items created by the current user and renders them 
    on the dashboard page.

    Args:
        HttpResponse: The rendered dashboard page with the list of items.
    """
    items = Item.objects.filter(created_by=request.user)
    return render(request, 'dashboard/index.html', {'items': items})
