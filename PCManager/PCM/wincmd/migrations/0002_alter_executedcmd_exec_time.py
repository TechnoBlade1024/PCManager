# Generated by Django 3.2.9 on 2021-11-08 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wincmd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executedcmd',
            name='exec_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 8, 9, 12, 11, 897556)),
        ),
    ]
