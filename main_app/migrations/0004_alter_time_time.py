# Generated by Django 3.2 on 2021-04-17 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='time',
            field=models.DurationField(),
        ),
    ]