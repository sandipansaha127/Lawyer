from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


ROLE_CHOICES = (('LAWYER', 'Lawyer'),('GUEST', 'Guest'))

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	role = models.CharField(max_length=6,choices=ROLE_CHOICES, null=False)

#celery

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	print(kwargs)
	if created:
		Profile.objects.create(user=instance,role=instance._role,birth_date=instance._birth_date,bio=instance._bio,location=instance._location)
	instance.profile.save()

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()