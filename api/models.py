from django.db import models
from django.contrib.auth.models import User

class work(models.Model):
    # owner
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    # description is defined for precession 
    description = models.TextField(max_length=200, null=True, blank=True, default=None)
    # completed is status of the task
    completed = models.BooleanField(default=False)
    last_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        # ordering based on tasks status & their last edit 
        # so, user can give priority to incomplete tasks!
        ordering = ['completed', '-last_edit']
