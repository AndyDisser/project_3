# Generated by Django 3.0.5 on 2020-05-02 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20200501_1526'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
