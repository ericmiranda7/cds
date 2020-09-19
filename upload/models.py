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

from criminals.models import Criminal

class UploadCriminal(Criminal):
    state = models.ForeignKey('States', on_delete=models.CASCADE, default=11)
    city = ChainedForeignKey(
        Cities,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        sort=True)
