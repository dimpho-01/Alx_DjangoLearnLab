from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    following = models.ManyToManyField(
        'self',
        through='UserFollow',
        symmetrical=False,
        related_name='followers',  # Users who follow the user
        through_fields=('user_from', 'user_to'),  # Correct order of the fields
    )
    
    def __str__(self):
        return self.username
    
class UserFollow(models.Model):
    user_from = models.ForeignKey(CustomUser, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(CustomUser, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)