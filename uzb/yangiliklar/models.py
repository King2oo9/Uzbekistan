from django.db import models
# Create your models here.
class yangiliklar(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'news'