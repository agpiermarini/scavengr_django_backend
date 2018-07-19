from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('id',)
