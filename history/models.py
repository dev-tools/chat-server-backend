from django.db import models

# Create your models here.
class User(models.Model):
   name = models.CharField(max_length=20)
class History(models.Model):
   date = models.DateTimeField('date sended')
   user = models.ForeignKey(User)
   message = models.CharField(max_length=2000)
