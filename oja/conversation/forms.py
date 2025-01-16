from django import forms
from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    """
    Form for creating and editing conversation messages.

    A ModelForm based on the ConversationMessage model that provides a styled
    textarea for message content input.

    Attributes:
        Meta: Configures the form's model, fields, and widgets
            model: ConversationMessage model
            fields: Only includes the 'content' field
            widgets: Customizes the textarea with Bootstrap styling
    """
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
                'content': forms.Textarea(attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Type your message here...'
                    })
                }
