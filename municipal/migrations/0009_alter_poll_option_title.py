# Generated by Django 4.2.6 on 2023-11-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('municipal', '0008_alter_poll_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll_option',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
