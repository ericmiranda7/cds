# Generated by Django 3.1 on 2020-09-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20200909_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcriminal',
            name='photo',
            field=models.ImageField(blank=True, default='criminals/missing.jpeg', upload_to='criminals/'),
        ),
    ]
