from django import forms
from django.core.exceptions import ValidationError
from .models import Item

INPUT_CLASSES = 'w-full py-2 px-3 rounded-xl border'

class NewItemForm(forms.ModelForm):
    """
    Form for creating a new item listing.

    This form handles the creation of new items with fields for category, name,
    description, price, and image. It includes validation for field lengths and
    price ranges.

    Attributes:
        Meta: Configures the form's model, fields, and widgets with custom styling.
    """
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
                'category': forms.Select(attrs={
                    'class': INPUT_CLASSES
                    }),
                
                'name': forms.TextInput(attrs={
                    'class': INPUT_CLASSES,
                    'maxlength': '15',
                    }),

                'description': forms.Textarea(attrs={
                    'class': INPUT_CLASSES,
                    'maxlength': '150',
                    'rows': 4
                    }),

                'price': forms.NumberInput(attrs={
                    'class': INPUT_CLASSES,
                    'max': '99999999',
                    'step': '0.01'
                    }),

                'image': forms.FileInput(attrs={
                    'class': INPUT_CLASSES,
                    'required': True,
                    })
                }
    def clean_price(self):
        """
        Validate the price field.

        Returns:
            float: The validated price value.

        Raises:
            ValidationError: If price exceeds 99,999,999 or is less than or equal to 0.
        """
        price = self.cleaned_data.get('price')
        if price >= 100000000:
            raise ValidationError('Price cannot exceed 99,999,999')
        if price <= 0:
            raise ValidationError('Price must be greater than 0')
        return price

    def clean_description(self):
        """
        Validate the description field.

        Returns:
            str: The validated description text.

        Raises:
            ValidationError: If description is empty or exceeds 150 characters.
        """
        description = self.cleaned_data.get('description')
        if not description:
            raise ValidationError('Description is required')
        if len(description) > 150:
            raise ValidationError('Description cannot exceed 150 characters')
        return description

    def clean_name(self):
        """
        Validate the name field.

        Returns:
            str: The validated name text.

        Raises:
            ValidationError: If name exceeds 15 characters.
        """
        name = self.cleaned_data.get('name')
        if len(name) > 15:
            raise ValidationError('Name cannot exceed 15 characters')
        return name

class EditItemForm(forms.ModelForm):
    """
    Form for editing an existing item listing.

    This form handles the modification of existing items with fields for name,
    description, price, image, and sold status. It includes validation for field
    lengths and price ranges.

    Attributes:
        Meta: Configures the form's model, fields, and widgets with custom styling.
    """
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold',)
        widgets = {
                'name': forms.TextInput(attrs={
                    'class': INPUT_CLASSES,
                    'maxlength': '15',
                    }),

                'description': forms.Textarea(attrs={
                    'class': INPUT_CLASSES,
                    'maxlength': '150',
                    'rows': 4
                    }),

                'price': forms.NumberInput(attrs={
                    'class': INPUT_CLASSES,
                    'step': '0.01'
                    }),

                'image': forms.FileInput(attrs={
                    'class': INPUT_CLASSES
                    }),
                }
    
    def clean_price(self):
        """
        Validate the price field.

        Returns:
            float: The validated price value.

        Raises:
            ValidationError: If price exceeds 99,999,999 or is less than or equal to 0.
        """
        price = self.cleaned_data.get('price')
        if price >= 100000000: 
            raise ValidationError('Price cannot exceed 99,999,999')
        if price <= 0:
            raise ValidationError('Price must be greater than 0')
        return price

    def clean_description(self):
        """
        Validate the description field.

        Returns:
            str: The validated description text.

        Raises:
            ValidationError: If description is empty or exceeds 150 characters.
        """
        description = self.cleaned_data.get('description')
        if not description:
            raise ValidationError('Description is required')
        if len(description) > 150:
            raise ValidationError('Description cannot exceed 150 characters')
        return description

    def clean_name(self):
        """
        Validate the name field.

        Returns:
            str: The validated name text.

        Raises:
            ValidationError: If name exceeds 15 characters.
        """
        name = self.cleaned_data.get('name')
        if len(name) > 15:
            raise ValidationError('Name cannot exceed 15 characters')
        return name

