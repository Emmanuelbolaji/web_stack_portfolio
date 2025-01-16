from django.apps import AppConfig

class ItemConfig(AppConfig):
    """
    Django application configuration for the item app.

    Defines the basic configuration settings for the item application.

    Attributes:
        default_auto_field (str): The default primary key field type for models
        name (str): The name of the Django application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'item'
