from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=30)
	nacionality = models.ManyToManyField('countries.Country') #Relaciones muchos a muchos
	father = models.OneToOneField('self', on_delete=models.CASCADE, null=True) #Relaciones uno a uno, null=True -> campo no obligatorio