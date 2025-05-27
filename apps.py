from django.apps import AppConfig


class CoffeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Coffee'
def ready(self):
        import Coffee.signals  