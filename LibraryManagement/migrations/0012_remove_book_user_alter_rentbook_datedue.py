# Generated by Django 4.1.4 on 2022-12-08 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagement', '0011_alter_rentbook_datedue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.AlterField(
            model_name='rentbook',
            name='dateDue',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 22, 17, 24, 39, 661384)),
        ),
    ]
