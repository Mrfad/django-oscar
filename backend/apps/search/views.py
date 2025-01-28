# apps/search/views.py
from django.views.generic import TemplateView
from oscar.core.loading import get_model, get_class
from apps.catalogue.models import Product  # Import your custom Product model

# Import Oscar's original CatalogueView without circular imports
OscarCatalogueView = get_class('search.views', 'CatalogueView')

class CatalogueView(OscarCatalogueView):
    """
    Override CatalogueView to filter by is_available.
    """

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_available=True)  # Use your custom field

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_variable'] = "Custom context variable"
        return context