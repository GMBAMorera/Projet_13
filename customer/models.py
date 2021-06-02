from django.db import models
from constants import STATUS_CHOICE

# Create your models here.


class Adress(models.Model):
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.number} {self.street}, {self.postal_code} {self.city} - {self.country}"


class WebAdress(models.Model):
    web_adress = models.URLField()
    site_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.site_name}: {self.web_adress}"


class VisitCard(models.Model):
    company = models.CharField(max_length=255)
    job = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)

    adress = models.ForeignKey(Adress, on_delete=models.CASCADE, null=True, blank=True)

    status = models.CharField(max_length=2, choices=STATUS_CHOICE, default='customer')

    def __str__(self):
        return f"{self.first_name} {self.surname}: {self.job} at {self.company}"


class PersonnalWebAdress(models.Model):
    web_adress = models.ForeignKey(WebAdress, on_delete=models.CASCADE)
    visit_card = models.ForeignKey(VisitCard, on_delete=models.CASCADE)
    description = models.TextField(blank=True)