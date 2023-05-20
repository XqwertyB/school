from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import News, Art

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ("name", "title")

@admin.register(Art)
class ArtAdmin(TranslationAdmin):
    pass
