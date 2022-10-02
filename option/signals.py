import translators as ts
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Option


@receiver(pre_save, sender=Option)
def translate(sender, instance, **kwargs):
    if not instance.name_en:
        translated_name = ts.google(instance.name, from_language='es', to_language='en')
        instance.name_en = translated_name.capitalize()
    
    if not instance.description_en:
        translated_description = ts.google(instance.description, from_language='es', to_language='en')
        instance.description_en = translated_description.capitalize()
