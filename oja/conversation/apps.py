from django.apps import AppConfig

class ConversationConfig(AppConfig):
    """
    Django application configuration for the conversation app.

    This class defines the basic configuration for the conversation application,
    including the default auto field type and application name.

    Attributes:
    default_auto_field (str): The default primary key field type for modelsdefault_auto_field (str): The default primary key field type for models
    name (str): The name of the Django application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'conversation'
