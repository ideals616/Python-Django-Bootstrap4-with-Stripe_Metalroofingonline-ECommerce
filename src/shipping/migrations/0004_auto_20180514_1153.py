# Generated by Django 2.0.3 on 2018-05-14 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0003_suburb'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('approx_delivery', models.IntegerField()),
                ('postal_code', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='shipping',
            old_name='zone_name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='suburb',
            name='delivery_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='suburb',
            name='postal_code',
            field=models.IntegerField(default=0),
        ),
    ]