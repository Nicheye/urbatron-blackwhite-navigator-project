# Generated by Django 4.2.6 on 2023-11-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0005_alter_citreport_react'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citreport',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]
