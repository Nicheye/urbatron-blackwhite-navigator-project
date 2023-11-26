# Generated by Django 4.2.6 on 2023-11-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_recentnew_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bis', models.CharField(choices=[('Student', 'Студент'), ('Worker', 'Рабочий'), ('Server', 'Служащий'), ('Retired', 'Пенисионер')], default='Worker', max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Мужчина'), ('Female', 'Женщина')], default='Female', max_length=6)),
                ('avatar', models.ImageField(default='./static/images/blank_logo.png', upload_to='avatars')),
            ],
        ),
    ]
