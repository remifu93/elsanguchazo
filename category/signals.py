import translators as ts
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Category


@receiver(pre_save, sender=Category)
def translate(sender, instance, **kwargs):
    if not instance.name_en:
        translated = ts.google(instance.name, from_language='es', to_language='en')
        instance.name_en = translated.capitalize()
