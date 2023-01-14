from django.db import models

# Create your models here.
class malumotlar(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    linkpicture = models.CharField(default='https://t3.ftcdn.net/jpg/00/61/40/40/360_F_61404050_Me0Y8GKi4MRsrOKR49ADO5EnEJgv2QtE.jpg',max_length=10000)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'malumot'
        verbose_name_plural = 'malumotlar'