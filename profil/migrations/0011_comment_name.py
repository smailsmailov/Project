# Generated by Django 3.2.4 on 2021-06-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.TextField(default=1, verbose_name='Ваш никнейм'),
            preserve_default=False,
        ),
    ]
