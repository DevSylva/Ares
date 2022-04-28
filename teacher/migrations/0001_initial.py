# Generated by Django 4.0.4 on 2022-04-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('function', models.CharField(max_length=150)),
                ('date_employed', models.DateField(auto_now=True)),
                ('avatar', models.ImageField(upload_to='')),
            ],
        ),
    ]
