# Generated by Django 2.2.5 on 2019-09-13 21:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20190913_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
