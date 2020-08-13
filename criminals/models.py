from django.db import models

# Create your models here.
class Criminal(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=3)
    pic = models.ImageField(blank=True)

    def __str__(self):
        return self.name