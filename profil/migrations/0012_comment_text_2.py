# Generated by Django 3.2.4 on 2021-06-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0011_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text_2',
            field=models.TextField(default=1, verbose_name='Коментарий!'),
            preserve_default=False,
        ),
    ]