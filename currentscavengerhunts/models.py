from django.db import models
from django.contrib.auth.models import User
from scavengerhunts.models import ScavengerHunt
from django.db.models.signals import post_save
from django.dispatch import receiver

class CurrentScavengerHunt(models.Model):
    scavenger_hunt  = models.ForeignKey(ScavengerHunt, on_delete=models.CASCADE)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at      = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Scavenger Hunt ID: {self.scavengerhunt.id}, User ID: {self.user.id}'

    class Meta:
        ordering = ('-created_at',)
