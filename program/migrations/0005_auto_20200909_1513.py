# Generated by Django 3.1 on 2020-09-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_auto_20200909_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(),
        ),
    ]
