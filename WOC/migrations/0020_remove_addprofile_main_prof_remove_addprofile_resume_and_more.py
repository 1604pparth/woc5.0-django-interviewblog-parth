# Generated by Django 4.1.5 on 2023-01-21 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WOC', '0019_alter_addprofile_placed_at_alter_addprofile_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addprofile',
            name='main_prof',
        ),
        migrations.RemoveField(
            model_name='addprofile',
            name='resume',
        ),
        migrations.AddField(
            model_name='addprofile',
            name='insta_prof',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='addprofile',
            name='linkedin_prof',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
