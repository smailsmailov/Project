# Generated by Django 3.2.4 on 2021-06-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0012_comment_text_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text_3',
            field=models.CharField(default=1, max_length=15, verbose_name='Время ответа'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='text_2',
            field=models.TextField(blank=True, verbose_name='Коментарий!'),
        ),
    ]