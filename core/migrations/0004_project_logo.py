# Generated by Django 4.0.4 on 2022-04-30 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
