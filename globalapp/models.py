from django.db import models

from authentication.models import User


class Projects(models.Model):
    project_type = [
        ('back-end', 'back-end'),
        ('front-end', 'front-end'),
        ('IOS', 'IOS'),
        ('Android', 'Android'),
    ]

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    type = models.CharField(max_length=16, choices=project_type)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
