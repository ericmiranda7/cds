from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from upload.models import States, Cities

# Create your models here.

class Criminal(models.Model):
    criminal_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    physical_description = models.TextField(blank=True)
    date = models.DateField()
    crime_type = models.CharField(max_length=30)
    arresting_agency = models.CharField(max_length=30)
    photo = models.ImageField(blank=True, upload_to='criminals/', default='criminals/missing.jpeg')
    status = models.TextField(blank=True, default='UNKNOWN')

    def __str__(self):
        return self.name
    
    def location(self):
        return self.city.name + ', ' + self.state.name

    class Meta:
        abstract = True
    


class VerifiedCriminal(Criminal):
    state = models.ForeignKey('upload.States', on_delete=models.CASCADE, default=11)
    city = ChainedForeignKey(
        Cities,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        sort=True)
    rating = models.FloatField(default=0)