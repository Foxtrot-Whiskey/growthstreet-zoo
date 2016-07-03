from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime
import uuid


class ZooCage:

    #uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    cage_contents = []

    def __init__(self, cage_type, cage_name):
        self.cage_type = cage_type
        self.cage_name = cage_name
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"

    def add_animal(self, animals):
        self.cage_contents.append(animals)



class ZooAnimal():

    #uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    animal_type = models.CharField(max_length=30)
    animal_name = models.CharField(max_length=30)
