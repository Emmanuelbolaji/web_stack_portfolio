from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    """
    Custom login form that extends Django's AuthenticationForm.
       
    This form provides styled login fields using Tailwind CSS classes for username
    and password inputs.

    Attributes:
        username (CharField): Field for user's username input with custom styling
        password (CharField): Field for user's password input with custom styling
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'
        }))


class SignupForm(UserCreationForm):
    """
    Custom user registration form extending Django's UserCreationForm.
       
    This form handles new user registration with custom styling and validation.
    Username is limited to 15 characters maximum.
    
    Attributes:
        username (CharField): Username field with 15 char limit and custom styling
        email (CharField): Email field with custom styling
        password1 (CharField): Password field with custom styling
        password2 (CharField): Password confirmation field with custom styling

    Meta:
        model: User model from django.contrib.auth.models
        fields: Tuple of fields to include in the form
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
            max_length=15,
            widget=forms.TextInput(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'
                })
            )
    def clean_username(self):
        """
        Validate the username field.
               
        Ensures username length is 15 characters or less.
                             
        Returns:
            str: The cleaned username if validation passes

        Raises:
            ValidationError: If username exceeds 15 characters
        """
        username = self.cleaned_data.get('username')
        if len(username) > 15:
            raise forms.ValidationError("Username must be 15 characters or less.")
        return username

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'
        }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'
        }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm'
        }))
