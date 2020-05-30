from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField (max_length=122)
    subject =models.CharField (max_length=200)
    desc =models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Apply(models.Model):

    des1=models.CharField(max_length=1000,default='cool')
    des2=models.CharField(max_length=1000,default='see')        


class Data(models.Model):   
     desc1 = models.CharField(max_length=1000,default='we')
     desc2 = models.CharField(max_length=1000,default='us')