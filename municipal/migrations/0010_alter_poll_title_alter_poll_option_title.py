# Generated by Django 4.2.6 on 2023-11-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipal', '0009_alter_poll_option_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='poll_option',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
