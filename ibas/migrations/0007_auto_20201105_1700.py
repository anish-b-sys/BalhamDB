# Generated by Django 3.0.8 on 2020-11-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibas', '0006_auto_20201105_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchtopic',
            name='Impact',
            field=models.TextField(max_length=60),
        ),
    ]