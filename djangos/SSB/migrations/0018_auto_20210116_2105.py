# Generated by Django 3.1.4 on 2021-01-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSB', '0017_products_careperiod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='carePeriod',
            field=models.IntegerField(default=0, verbose_name='Bakım Periyodu (gün)'),
        ),
    ]