import uuid
from django.db import models

class ZooAnimal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    animal_type = models.CharField(max_length=30)
    animal_name = models.CharField(max_length=30)

#
'''class Animal(models.Model):
    CAT = 'CA'
    DOG = 'DO'
    ELEPHANT = 'EL'
    BEAR = 'BE'
    ANIMAL_CHOICES = (
        (CAT, 'Cat'),
        (DOG, 'Dog'),
        (ELEPHANT, 'Elephant'),
        (BEAR, 'Bear'),
    )
    animals = models.CharField(
            max_length=2,
            choices=ANIMAL_CHOICES,
            default=DOG,
        )
    def is_pet(self):
            return self.animals in (self.CAT, self.DOG)
