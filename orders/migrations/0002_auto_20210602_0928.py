# Generated by Django 3.1.6 on 2021-06-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='vendor_paid',
        ),
        migrations.AddField(
            model_name='order',
            name='vendors',
            field=models.ManyToManyField(related_name='orders', to='vendor.Vendor'),
        ),
    ]
