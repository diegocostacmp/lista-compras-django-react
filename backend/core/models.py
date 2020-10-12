from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE())
    name = models.CharField(max_length=50)

    def __init__(self):
        return self.name
