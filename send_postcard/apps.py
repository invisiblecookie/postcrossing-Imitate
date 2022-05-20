from django.apps import AppConfig


class SendPostcardConfig(AppConfig):
    name = 'send_postcard'

    def ready(self):
        import send_postcard.signals