# Generated by Django 4.1.5 on 2023-01-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WOC', '0029_post_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='+', to='WOC.profile'),
        ),
    ]
