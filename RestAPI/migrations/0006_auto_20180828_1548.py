# Generated by Django 2.0.7 on 2018-08-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestAPI', '0005_auto_20180828_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
