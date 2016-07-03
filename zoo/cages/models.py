from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import datetime
import uuid


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class ZooCage(models.Model):
    #uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    cage_type = models.CharField(max_length=200)
    cage_name = models.CharField(max_length=200)
    cage_contents = []

    def add_animal(self, animals):
        self.cage_contents.append(animals)



class ZooAnimal(models.Model):

    #uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    animal_type = models.CharField(max_length=30)
    animal_name = models.CharField(max_length=30)
