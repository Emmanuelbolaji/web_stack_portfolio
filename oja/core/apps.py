from django.apps import AppConfig

class CoreConfig(AppConfig):
    """
    Django application configuration for the core app.
        
    This class defines the basic configuration for the core application,
    including the default auto field type for model primary keys and
    the application name.
                        
    Attributes:
        default_auto_field (str): The default primary key field type to use
            for models that don't specify a primary key field. Set to use
            BigAutoField for improved scalability.
        name (str): The name of the Django application, used for app registry
            and Django's internal references.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
