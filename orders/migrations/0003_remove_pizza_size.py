# Generated by Django 3.0.5 on 2020-04-12 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200412_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='size',
        ),
    ]