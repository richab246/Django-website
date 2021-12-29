from django.db import models
# from django.db.models.fields import CharField

# Create your models here.
class Contact(models.Model):
   name = models.CharField(max_length=122)
   email = models.CharField(max_length=122)
   phone = models.CharField(max_length=12)
   password = models.CharField(max_length=122)
   date = models.DateField()

   def __str__(self):
       return self.name
