# Generated by Django 4.2.6 on 2023-11-26 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='attends',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='comments',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='elo',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='votes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
