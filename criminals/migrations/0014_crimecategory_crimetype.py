# Generated by Django 3.1 on 2020-09-21 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0013_auto_20200919_0602'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrimeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='CrimeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=16)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criminals.crimecategory')),
            ],
        ),
    ]
