# Generated by Django 4.0.6 on 2022-07-21 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0002_alter_visit_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='visit_date',
            field=models.DateField(default=datetime.datetime(2022, 7, 21, 12, 55, 26, 41254)),
        ),
    ]
