# Generated by Django 2.1.7 on 2019-05-05 07:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0003_auto_20190502_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_time',
            field=models.IntegerField(help_text='Enter value in 24 hour format', validators=[django.core.validators.MaxValueValidator(23), django.core.validators.MinValueValidator(0)]),
        ),
    ]
