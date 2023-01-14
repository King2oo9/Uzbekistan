from django.db import models


# Create your models here.

class Contact(models.Model):
    ism = models.CharField(max_length=100)
    mavzu = models.CharField(max_length=1000)
    matn = models.TextField()

    def __str__(self):
        return self.ism
