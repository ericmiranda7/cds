# Generated by Django 3.1 on 2020-08-19 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contactus.contact')),
            ],
        ),
    ]
