# Generated by Django 3.0.5 on 2020-04-30 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0019_orderpizza_toppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpizza',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders_pizza', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='OrderSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('additons', models.ManyToManyField(blank=True, null=True, to='orders.Addition')),
                ('sub', models.ManyToManyField(to='orders.Subs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders_sub', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
