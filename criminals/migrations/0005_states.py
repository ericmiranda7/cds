# Generated by Django 3.1 on 2020-08-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0004_auto_20200819_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country_id', models.IntegerField()),
            ],
        ),
    ]
