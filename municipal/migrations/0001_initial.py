# Generated by Django 4.2.6 on 2023-11-24 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Munic_works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('dead_line_date', models.DateField()),
                ('opt_image', models.ImageField(blank=True, upload_to='munic_works_schedule_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Type_of_munic_works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=12)),
            ],
        ),
    ]
