# Generated by Django 4.1.5 on 2023-01-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WOC', '0021_addprofile_main_prof_alter_addprofile_insta_prof_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addprofile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumes'),
        ),
    ]
