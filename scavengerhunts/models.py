from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ScavengerHunt(models.Model):
    name        = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=250, blank=False)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at  = models.DateField(auto_now_add=True)
    updated_at  = models.DateField(auto_now=True)

    def username(self):
        return self.user.username

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
