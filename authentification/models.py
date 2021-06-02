
from customer.models import VisitCard
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    visit_card = models.ForeignKey(VisitCard, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}"