# Generated by Django 3.1 on 2020-09-21 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0010_merge_20200921_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadcriminal',
            name='fir',
        ),
        migrations.RemoveField(
            model_name='uploadcriminal',
            name='fir_no',
        ),
    ]
