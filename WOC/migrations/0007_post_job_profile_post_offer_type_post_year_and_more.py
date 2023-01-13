# Generated by Django 4.1.5 on 2023-01-13 09:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('WOC', '0006_alter_post_id_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='job_profile',
            field=models.CharField(default='Software Engineer', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='offer_type',
            field=models.CharField(default='Internship Only', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='year',
            field=models.IntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('be4c72e9-89fa-4d38-83b7-d7e5f98a1b45'), primary_key=True, serialize=False),
        ),
    ]
