# Generated by Django 2.0.5 on 2019-02-10 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_cart_date_delivered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='date_delivered',
            new_name='delivery_date',
        ),
    ]