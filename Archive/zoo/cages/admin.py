from django.contrib import admin

# Register your models here.

from .models import Question, ZooCage

admin.site.register(Question)
admin.site.register(ZooCage)
