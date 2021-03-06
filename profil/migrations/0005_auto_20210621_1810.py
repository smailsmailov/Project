# Generated by Django 3.2.4 on 2021-06-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0004_auto_20210621_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autem',
            name='image',
            field=models.ImageField(default=None, upload_to='', verbose_name='Главная фотография'),
        ),
        migrations.AlterField(
            model_name='autem',
            name='image1',
            field=models.ImageField(blank=True, default=None, upload_to='', verbose_name='Фото номер 1'),
        ),
        migrations.AlterField(
            model_name='autem',
            name='image2',
            field=models.ImageField(blank=True, default=None, upload_to='', verbose_name='Фото номер 2'),
        ),
        migrations.AlterField(
            model_name='autem',
            name='image3',
            field=models.ImageField(blank=True, default=None, upload_to='', verbose_name='Фото номер 3'),
        ),
        migrations.AlterField(
            model_name='autem',
            name='image4',
            field=models.ImageField(blank=True, default=None, upload_to='', verbose_name='Фото номер 4'),
        ),
    ]
