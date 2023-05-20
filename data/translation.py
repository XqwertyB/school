from modeltranslation.translator import register, TranslationOptions
from .models import News, Art

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'title')

@register(Art)
class ArtTranslationOptions(TranslationOptions):
    fields = ('name',)





