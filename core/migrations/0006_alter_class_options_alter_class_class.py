# Generated by Django 4.0.4 on 2022-04-15 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_class'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterField(
            model_name='class',
            name='Class',
            field=models.CharField(max_length=50),
        ),
    ]
