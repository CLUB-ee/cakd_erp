from django.apps import AppConfig


class ErpConfig(AppConfig):
    name = 'erp'
    def ready(self):
        import erp.singnal
