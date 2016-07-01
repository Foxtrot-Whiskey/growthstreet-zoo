from django.db import models
from django.db.models import Q, Sum
from django.utils import timezone

class Animal(models.Model):
    '''
    Animal - has id, type, name
    '''
