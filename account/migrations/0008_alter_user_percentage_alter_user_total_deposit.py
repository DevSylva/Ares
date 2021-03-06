# Generated by Django 4.0.4 on 2022-06-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_account_balance_alter_user_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='percentage',
            field=models.CharField(blank=True, default='0', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='total_deposit',
            field=models.FloatField(default=0),
        ),
    ]
