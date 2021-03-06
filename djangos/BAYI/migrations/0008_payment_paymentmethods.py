# Generated by Django 3.1.5 on 2021-01-16 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SSB', '0018_auto_20210116_2105'),
        ('BAYI', '0007_auto_20210116_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentName', models.CharField(max_length=100, verbose_name='Ödeme Yöntemi')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentAmount', models.FloatField(default=0, verbose_name='Ödeme Miktarı')),
                ('paymentNot', models.CharField(max_length=100, verbose_name='Ödeme Notu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SSB.orders', verbose_name='Bayi Siparişeri')),
                ('paymentName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BAYI.paymentmethods', verbose_name='Ödeme Yöntemi')),
            ],
        ),
    ]
