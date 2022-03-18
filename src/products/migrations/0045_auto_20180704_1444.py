# Generated by Django 2.0.5 on 2018-07-04 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0044_auto_20180703_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='preload_colours',
            field=models.BooleanField(default=False, help_text='Add all colours to product'),
        ),
        migrations.AddField(
            model_name='product',
            name='preload_lengths',
            field=models.BooleanField(default=False, help_text='Add all lengths to product'),
        ),
    ]