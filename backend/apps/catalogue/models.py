from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    is_available = models.BooleanField(default=True)

from oscar.apps.catalogue.models import * 
