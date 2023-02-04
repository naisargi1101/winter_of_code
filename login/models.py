from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    userId = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE )
    userBatch = models.CharField(max_length=150, null=True, blank=True)
    userCourse = models.CharField(max_length=150, null=True, blank=True)


# When any User instance created, Profile object instance is created automatically linked by User 
@receiver(post_save, sender = User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)
    else:
        instance.profile.save()
