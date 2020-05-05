# Generated by Django 3.0.5 on 2020-05-02 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0025_auto_20200502_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkouts',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='user_checkouts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
