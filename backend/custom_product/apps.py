from django.apps import AppConfig
from oscar.apps.catalogue.apps import CatalogueConfig as OscarCatalogueConfig


class CustomProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_product'
