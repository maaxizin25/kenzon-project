from django.apps import AppConfig


class CarrinhosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "carrinhos"

    def ready(self):
        import carrinhos.signals
