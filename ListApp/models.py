from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ListTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    title = models.CharField(max_length=30, null=True)
    desc = models.TextField(max_length=200, null=True)
    complet = models.BooleanField(default=False)
    time =models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self) -> str:
        return str(self.title)