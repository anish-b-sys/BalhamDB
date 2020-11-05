# Generated by Django 3.0.8 on 2020-11-05 04:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibas', '0008_auto_20201105_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='MaximumMark',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(10)]),
        ),
    ]
