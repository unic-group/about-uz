# Generated by Django 4.2.4 on 2023-09-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyplacedetail',
            name='image1_1',
            field=models.ImageField(default=0, upload_to='histoy_place_photo', verbose_name='Tarixiy joy rasmi: '),
            preserve_default=False,
        ),
    ]
