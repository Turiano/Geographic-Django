from django.db import models

# Create your models here.
class Country(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=5)

def __str__(self):
    return self.name
		