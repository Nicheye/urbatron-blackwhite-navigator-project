# Generated by Django 4.2.6 on 2023-11-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='commonpost',
            name='date',
            field=models.CharField(blank=True, default='21.10.2023', max_length=10000),
        ),
        migrations.AddField(
            model_name='commonpost',
            name='link',
            field=models.CharField(blank=True, default='https://google.com', max_length=10000),
        ),
        migrations.AddField(
            model_name='commonpost',
            name='place',
            field=models.CharField(default='Msc', max_length=70),
        ),
        migrations.AddField(
            model_name='commonpost',
            name='time',
            field=models.CharField(blank=True, default='23:05', max_length=10000),
        ),
    ]
