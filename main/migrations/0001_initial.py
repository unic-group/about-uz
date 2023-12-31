# Generated by Django 4.2.4 on 2023-09-06 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Viloyat nomi (uz): ')),
                ('image_region', models.ImageField(upload_to='region_photo', verbose_name='Viloyat asosiy rasmi: ')),
                ('teg', models.CharField(max_length=150, verbose_name='Viloyat tegi (uz): ')),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
            },
        ),
        migrations.CreateModel(
            name='RegionDetailPhotoZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Fotozona lar haqida: ')),
                ('map', models.TextField(verbose_name='Fotozonalar xaritasi: ')),
                ('image', models.ImageField(upload_to='photo_zone_image', verbose_name='Fotozona rasmi: ')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='Viloyatni tanlang: ')),
            ],
        ),
        migrations.CreateModel(
            name='RegionDetailPhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photogallery', verbose_name='Viloyat Rasmi: ')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='Viloyatni tanlang: ')),
            ],
        ),
        migrations.CreateModel(
            name='RegionDetailHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Viloyat tarixi haqida: ')),
                ('image', models.ImageField(upload_to='history_photo', verbose_name='Viloyat tarixi rasmi: ')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='Viloyatni tanlang: ')),
            ],
        ),
        migrations.CreateModel(
            name='RegionDetailGiftImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gift_photo', verbose_name='Sovga va suvinerlar rasmi: ')),
                ('gift', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='sovga va suvinerlar : ')),
            ],
        ),
        migrations.CreateModel(
            name='RegionDetailGift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Sovga va suvinerlar haqida: ')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='Viloyatni tanlang: ')),
            ],
        ),
        migrations.CreateModel(
            name='RegionDetailFoodPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='food_photo', verbose_name='Milliy taomlar: ')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='Viloyatni tanlang: ')),
            ],
        ),
        migrations.CreateModel(
            name='RegionDetailFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Viloyat milliy taomlari haqida : ')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='Viloyatni tanlang: ')),
            ],
        ),
        migrations.CreateModel(
            name='RegionDetailClimate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Iqlim haqida: ')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='Viloyatni tanlang: ')),
            ],
        ),
        migrations.CreateModel(
            name='RegionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decription', models.TextField(verbose_name='Viloyat haqida: ')),
                ('image_header', models.ImageField(upload_to='image_header', verbose_name='Viloyat header rasmi: ')),
                ('image', models.ImageField(upload_to='region_photo', verbose_name='viloyat rasmi: ')),
                ('map', models.TextField(verbose_name='Vioyat xaritasi: ')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='Viloyatni tanlang: ')),
            ],
            options={
                'verbose_name': 'Viloyat malumoti',
                'verbose_name_plural': 'Viloyatlar malumoti',
            },
        ),
        migrations.CreateModel(
            name='HistoryPlaceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='tarixiy joy nomi: ')),
                ('image_header', models.ImageField(upload_to='header_photo', verbose_name='Header rasmi: ')),
                ('title1', models.TextField(verbose_name='tarixiy joy haqida (1): ')),
                ('image1', models.ImageField(upload_to='histoy_place_photo', verbose_name='Tarixiy joy rasmi: ')),
                ('title2', models.TextField(verbose_name='tarixiy joy haqida (2): ')),
                ('image2', models.ImageField(upload_to='histoy_place_photo', verbose_name='Tarixiy joy rasmi: ')),
                ('title3', models.TextField(verbose_name='Tarixiy joy haqida (3): ')),
                ('image3', models.ImageField(upload_to='', verbose_name='tarixiy joy rasmi (3): ')),
                ('map', models.TextField(verbose_name='Joylashuv qismi karta: ')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='Viloyatni tanlang: ')),
            ],
        ),
    ]
