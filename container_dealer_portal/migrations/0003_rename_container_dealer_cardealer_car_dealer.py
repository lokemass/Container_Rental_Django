# Generated by Django 3.2.9 on 2021-11-18 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('container_dealer_portal', '0002_cardealer_wallet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardealer',
            old_name='container_dealer',
            new_name='car_dealer',
        ),
    ]