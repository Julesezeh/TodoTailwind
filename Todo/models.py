from django.db import models
from User.models import CustomUser
# Create your models here.


class Todo(models.Model):
    task = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_due = models.DateTimeField()
    is_active = models.BooleanField()
    