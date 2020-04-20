# Generated by Django 3.0.5 on 2020-04-12 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_pizza_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subs',
            name='price',
        ),
        migrations.AddField(
            model_name='subs',
            name='price_large',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
        migrations.AddField(
            model_name='subs',
            name='price_small',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]