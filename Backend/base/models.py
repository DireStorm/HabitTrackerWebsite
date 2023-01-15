from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # id_ = User.id
    # birth_date = models.DateField(null=True, blank=True)
    score = models.PositiveIntegerField(default=0, blank=True) 
    #^Might run into errors with this because values sent from server can be negative
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("Profile was created!")
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print(f"Profile was saved, and the score is {instance.profile.score}")
    instance.profile.save()
