# Generated by Django 4.1.5 on 2023-01-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WOC', '0012_addprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addprofile',
            name='ctc',
            field=models.IntegerField(),
        ),
    ]
