# Generated by Django 2.0.3 on 2018-05-07 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20180502_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessoryoption',
            name='zincalume_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
    ]