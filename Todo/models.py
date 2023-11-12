from django.db import models
from User.models import CustomUser
# Create your models here.


class Todo(models.Model):
    task = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    #Send notification to the User's email when the time starts to get close (30 minutes before)
    time_due = models.DateTimeField()
    is_active = models.BooleanField()

    # Pin to the top if true
    is_pinned = models.BooleanField(default=False)



    def __str__(self):
        return f"Task: {self.task}\nDue: {self.time_due}"