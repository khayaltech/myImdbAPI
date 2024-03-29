from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def create_token(sender,instance, created,**kwargs):
  if created:
    Token.objects.create(user=instance)