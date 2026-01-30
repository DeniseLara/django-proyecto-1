from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    commercial = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Interaction(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="interactions"
    )
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return f"Interaction - {self.client.name}"
