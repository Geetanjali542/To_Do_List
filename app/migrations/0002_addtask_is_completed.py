# Generated by Django 5.0.6 on 2024-05-24 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtask',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
