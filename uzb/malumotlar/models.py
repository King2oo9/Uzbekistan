from django.db import models

# Create your models here.
class malumotlar(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    linkpicture = models.ImageField(default='')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'malumot'
        verbose_name_plural = 'malumotlar'