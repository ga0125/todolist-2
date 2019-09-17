from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=55, blank=False, null=False)
    desc = models.CharField(max_length=100, blank=True, null=False)
    deadline = models.DateField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    filed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
