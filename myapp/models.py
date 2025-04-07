from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    pass


class Stock(models.Model):
    """
    Model representing the list of Stocks to be tracked
    """
    symbol = models.CharField(max_length=12, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    notes = models.CharField(max_length=1024, blank=True)
    img = models.ImageField(upload_to='myapp/', null="True", blank="True")

    class Meta:
        ordering = ["symbol"]

    def __str__(self):
        return f"{self.symbol} - {self.name}"

    def get_absolute_url(self):
        """ Displays the values submitted following the DB update """
        return reverse("update", kwargs={'pk':self.pk})

    def clean(self):
        """ Ensure the Symbol is converted to Uppercase before saving the record """
        self.symbol = self.symbol.upper()