from django.shortcuts import render, redirect
from .forms import SignupForm

def contact(request):
    """
    View function to render the contact page.

    Args:
        request (HttpRequest): The HTTP request object
    Returns:
        HttpResponse: Rendered contact.html template
    """
    return render(request, 'core/contact.html')

def signup(request):
    """
    View function to handle user registration.
       
    Handles both GET and POST requests:
    - GET: Displays empty signup form
    - POST: Processes form submission, creates new user if valid
                   
    Args:
        request (HttpRequest): The HTTP request object

    Returns:
        HttpResponse:
            - On GET: Rendered signup form
            - On POST with valid data: Redirect to login page
            - On POST with invalid data: Rendered signup form with errors

    Context:
        form (SignupForm): The user registration form
            - Empty form for GET requests
            - Populated form with errors for invalid POST requests
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')

    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
        })
