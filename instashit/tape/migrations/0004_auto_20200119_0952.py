# Generated by Django 3.0.1 on 2020-01-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tape', '0003_auto_20200118_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='commets',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.CharField(max_length=2000, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', max_length=256, upload_to='static/img/posts', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='post',
            name='like_count',
            field=models.PositiveIntegerField(null=True, verbose_name='Количество лайков'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, max_length=256, null=True, upload_to='static/img/avatars', verbose_name='Аватар'),
        ),
    ]
