from ast import Add
from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models.auth import User,Profile

@receiver(post_save,sender=User)
def create_profile_and_address(sender,**kwargs):
    created = kwargs.get('created')
    user = kwargs.get('instance')
    if created:
        Profile.objects.create(user=user)
    





