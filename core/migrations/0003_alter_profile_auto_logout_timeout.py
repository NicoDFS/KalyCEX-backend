# Generated by Django 3.2.7

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='auto_logout_timeout',
            field=models.IntegerField(default=1440),
        ),
    ]
