# Generated by Django 4.1.5 on 2023-01-23 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WOC', '0030_alter_post_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked_by',
        ),
    ]
