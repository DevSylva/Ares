# Generated by Django 4.0.4 on 2022-06-19 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_payment_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='daily_interest',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]