# Generated by Django 3.2.18

import core.currency
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20230413_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('base', core.currency.CurrencyModelField()),
                ('quote', core.currency.CurrencyModelField()),
            ],
        )
    ]