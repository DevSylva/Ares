# Generated by Django 4.0.4 on 2022-07-24 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_payment_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='receipt',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
