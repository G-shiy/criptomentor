# Generated by Django 3.2.12 on 2022-06-11 21:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='created_at',
            field=models.DateField(auto_created=datetime.datetime.now),
        ),
    ]
