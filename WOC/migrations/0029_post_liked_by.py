# Generated by Django 4.1.5 on 2023-01-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WOC', '0028_remove_post_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_by',
            field=models.ManyToManyField(related_name='+', to='WOC.profile'),
        ),
    ]
