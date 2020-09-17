from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class States(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Cities(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey('States', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UploadCriminal(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    physical_description = models.TextField(blank=True)
    date = models.DateField()
    state = models.ForeignKey('States', on_delete=models.CASCADE, default=11)
    city = ChainedForeignKey(
        Cities,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        sort=True)
    crime_type = models.CharField(max_length=30)
    arresting_agency = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='criminals/', blank=True, default='criminals/missing.jpeg')
    status = models.TextField(blank=True, default='UNKNOWN')
    fir_no = models.IntegerField()
    fir = models.FileField(upload_to='fir/')