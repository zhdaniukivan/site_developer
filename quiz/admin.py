from django.contrib import admin
from quiz.models import Level, Language,Questions

# Register your models here.

admin.site.register(Language)
admin.site.register(Level)
admin.site.register(Questions)

