# Generated by Django 3.2.7

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocoins', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BTCWithdrawalApprove',
        ),
        migrations.DeleteModel(
            name='ETHWithdrawalApprove',
        ),
    ]
