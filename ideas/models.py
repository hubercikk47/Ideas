from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


IDEA_STATUS = [
    ('draft', 'Draft'),
    ('review', 'Under Review'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
]


class Idea(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    status = models.CharField(choices=IDEA_STATUS, max_length=15)
    date = models.DateField(null=False, default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.author}"


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    content = models.TextField()
    date = models.DateField(null=False, default=timezone.now)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} - {self.idea}"





