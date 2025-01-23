from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import customTableRevHistory

@receiver(pre_save)
def create_revision_history(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        for field in instance._meta.fields:
            field_name = field.name
            old_value = getattr(old_instance, field_name)
            new_value = getattr(instance, field_name)
            if old_value != new_value:

                customTableRevHistory.objects.create(
                    table=instance,
                    column_name=field_name,
                    old_value=old_value,
                    new_value=new_value,
                    change_date=timezone.now()
                    )
