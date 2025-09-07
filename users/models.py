from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("super_admin", "Super Admin"),
        ("enumerator", "Enumerator"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="enumerator")

    def __str__(self):
        return f"{self.username} ({self.role})"
