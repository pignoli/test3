# Generated by Django 3.2 on 2022-04-17 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phto',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
