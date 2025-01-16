from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator

class Category(models.Model):
    """
    Model representing item categories in the marketplace.

    This model stores the different categories that items can belong to,
    with basic information like the category name.

    Attributes:
        name (str): The name of the category, limited to 255 characters.

    Meta:
        ordering: Orders categories alphabetically by name
        verbose_name_plural: Sets plural form as 'Categories'
    """
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        """
        String representation of the Category model.

        Returns:
            str: The category name
        """

class Item(models.Model):
    """
    Model representing items listed in the marketplace.

    This model stores all information about items that users can list for sale,
    including details like category, name, description, price, and status.

    Attributes:
        category (Category): ForeignKey reference to the Category model
        name (str): Name of the item, limited to 15 characters
        description (str): Description of the item, limited to 150 characters
        price (float): Price of the item, maximum 8 digits (99,999,999)
        image (ImageField): Item's image, uploads to 'item_images' directory
        is_sold (bool): Flag indicating if the item has been sold
        created_by (User): ForeignKey reference to the User who created the listing
        created_at (datetime): Timestamp of when the item was listed
    """
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    description = models.TextField(
            max_length=150,
            blank=False
            )
    price = models.FloatField(validators=[MaxValueValidator(99999999)])
    image = models.ImageField(
            upload_to='item_images',
            default='item_images/default.jpg'
            )
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the Item model.

        Returns:
            str: The item name

        Note:
            There appears to be a typo in the original code (nam instead of name)
            which should be fixed.
        """
        return self.name
