# Generated by Django 3.2.7 

import seo.validators
from django.db import migrations, models
import django.utils.timezone
import lib.fields
import core.currency


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('announce_image', models.ImageField(upload_to=seo.validators.upload_to, validators=[seo.validators.validate_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(default='', max_length=255)),
                ('name_ru', models.CharField(default='', max_length=255, null=True)),
                ('name_en', models.CharField(default='', max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('meta_title', models.TextField(blank=True, default=None, null=True)),
                ('meta_title_ru', models.TextField(blank=True, default=None, null=True)),
                ('meta_title_en', models.TextField(blank=True, default=None, null=True)),
                ('meta_description', models.TextField(blank=True, default=None, null=True)),
                ('meta_description_ru', models.TextField(blank=True, default=None, null=True)),
                ('meta_description_en', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('slug_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('slug_en', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('title_ru', models.TextField(blank=True, null=True)),
                ('title_en', models.TextField(blank=True, null=True)),
                ('text', lib.fields.RichTextField(blank=True, null=True)),
                ('text_ru', lib.fields.RichTextField(blank=True, null=True)),
                ('text_en', lib.fields.RichTextField(blank=True, null=True)),
                ('preview_image', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/preview/')),
                ('views_count', models.PositiveIntegerField(blank=True, default=0)),
                ('meta_title', models.TextField(blank=True, null=True)),
                ('meta_title_ru', models.TextField(blank=True, null=True)),
                ('meta_title_en', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('meta_description_ru', models.TextField(blank=True, null=True)),
                ('meta_description_en', models.TextField(blank=True, null=True)),
                ('tags', models.ManyToManyField(to='seo.Tag')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),

        migrations.CreateModel(
            name='CoinStaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', core.currency.CurrencyModelField(unique=True)),
                ('title', models.CharField(blank=True, default='', max_length=511, verbose_name='Page title')),
                ('title_ru',
                 models.CharField(blank=True, default='', max_length=511, null=True, verbose_name='Page title')),
                ('title_en',
                 models.CharField(blank=True, default='', max_length=511, null=True, verbose_name='Page title')),
                ('name', models.CharField(max_length=255, verbose_name='Currency name (e.g. Bitcoin)')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Currency name (e.g. Bitcoin)')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Currency name (e.g. Bitcoin)')),
                ('trade_button_text',
                 models.CharField(blank=True, default='', max_length=511, verbose_name='Header trade button text')),
                ('trade_button_text_ru', models.CharField(blank=True, default='', max_length=511, null=True,
                                                          verbose_name='Header trade button text')),
                ('trade_button_text_en', models.CharField(blank=True, default='', max_length=511, null=True,
                                                          verbose_name='Header trade button text')),
                ('meta_description', models.TextField(blank=True, default='')),
                ('meta_description_ru', models.TextField(blank=True, default='', null=True)),
                ('meta_description_en', models.TextField(blank=True, default='', null=True)),
                ('header_text', lib.fields.RichTextField()),
                ('header_text_ru', lib.fields.RichTextField(null=True)),
                ('header_text_en', lib.fields.RichTextField(null=True)),
                ('usd_block_text', lib.fields.RichTextField(blank=True, default='')),
                ('usd_block_text_ru', lib.fields.RichTextField(blank=True, default='', null=True)),
                ('usd_block_text_en', lib.fields.RichTextField(blank=True, default='', null=True)),
                ('eur_block_text', lib.fields.RichTextField(blank=True, default='')),
                ('eur_block_text_ru', lib.fields.RichTextField(blank=True, default='', null=True)),
                ('eur_block_text_en', lib.fields.RichTextField(blank=True, default='', null=True)),
                ('rub_block_text', lib.fields.RichTextField(blank=True, default='')),
                ('rub_block_text_ru', lib.fields.RichTextField(blank=True, default='', null=True)),
                ('rub_block_text_en', lib.fields.RichTextField(blank=True, default='', null=True)),
                ('footer_text', lib.fields.RichTextField()),
                ('footer_text_ru', lib.fields.RichTextField(null=True)),
                ('footer_text_en', lib.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoinStaticSubPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', core.currency.CurrencyModelField()),
                ('slug', models.CharField(blank=True, default='', max_length=255)),
                ('slug_ru', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('slug_en', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('title', models.CharField(blank=True, default='', max_length=255)),
                ('title_ru', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('content', lib.fields.RichTextField(blank=True, default='')),
                ('content_ru', lib.fields.RichTextField(blank=True, default='', null=True)),
                ('content_en', lib.fields.RichTextField(blank=True, default='', null=True)),
                ('meta_title', models.TextField(blank=True, default='')),
                ('meta_title_ru', models.TextField(blank=True, default='', null=True)),
                ('meta_title_en', models.TextField(blank=True, default='', null=True)),
                ('meta_description', models.TextField(blank=True, default='')),
                ('meta_description_ru', models.TextField(blank=True, default='', null=True)),
                ('meta_description_en', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
