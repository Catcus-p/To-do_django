from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = RichTextField()
    description = RichTextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        