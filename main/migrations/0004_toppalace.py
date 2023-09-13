# Generated by Django 4.2.4 on 2023-09-12 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopPalace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Diqqatga sazovor joy nomi: ')),
                ('image_header', models.ImageField(upload_to='attractions_photo_header', verbose_name='Diqqatga sazovor joylar header rasmi: ')),
                ('image1', models.ImageField(upload_to='attracions_photo1', verbose_name='Diqqatga sazovor joylar rasmi (1): ')),
                ('image2', models.ImageField(upload_to='attracions_photo2', verbose_name='Diqqatga sazovor joylar rasmi (2): ')),
                ('image3', models.ImageField(upload_to='attracions_photo3', verbose_name='Diqqatga sazovor joylar rasmi (3): ')),
                ('image4', models.ImageField(upload_to='attracions_photo4', verbose_name='Diqqatga sazovor joylar rasmi (4): ')),
                ('title1', models.TextField(verbose_name='Diqqatga sazovor joylar haqida (1): ')),
                ('title2', models.TextField(verbose_name='Diqqatga sazovor joylar haqida (2): ')),
                ('title3', models.TextField(verbose_name='Diqqatga sazovor joylar haqida (3): ')),
                ('map', models.TextField(verbose_name='Diqqatga sazovor joylar manzili: ')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.region', verbose_name='Viloyatni tanlang: ')),
            ],
        ),
    ]
