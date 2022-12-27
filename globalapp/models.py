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
    description = models.CharField(max_length=1024)
    type = models.CharField(max_length=16, choices=project_type)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author_project_id')

    def __str__(self):
        return self.title


class Contributors(models.Model):
    PERMISSION = [('author', 'author'),
                  ('contributeur', 'contributeur')]

    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    permission = models.CharField(max_length=64, choices=PERMISSION)
    role = models.CharField(max_length=64)

    def __str__(self):
        return self.user_id


class Issues(models.Model):

    priorite = [
        ('FAIBLE', 'Faible'),
        ('MOYENNE', 'Moyenne'),
        ('ELEVE', 'Elevée')
    ]
    balise = [
        ('BUG','BUG'),
        ('AMELIORATION', 'Amélioration'),
        ('TACHE', 'Tâche')
    ]
    statut = [
        ('A faire', 'A faire'),
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé')
    ]

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    tag = models.CharField(max_length=16, choices=balise)
    priority = models.CharField(max_length=16, choices=priorite)
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    stats = models.CharField(max_length=16, choices=statut)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author_issue_id')
    Assignee_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='assignee_issue_id')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    description = models.CharField(max_length=1024)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey(to=Issues, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
