from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractCategory

class Category(AbstractCategory):
    pass

class Product(AbstractProduct):
    is_available = models.BooleanField(default=True)

from oscar.apps.catalogue.models import * 
