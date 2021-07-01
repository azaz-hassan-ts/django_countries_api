from django.db import models

# Create your models here.

class Countries(models.Model):
    name = models.TextField()
    capital = models.TextField()

    def __str__(self):
        return f"name: {self.name} - capital: {self.capital}"