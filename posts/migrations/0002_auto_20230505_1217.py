# Generated by Django 3.2.18 on 2023-05-05 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='place_id',
            field=models.CharField(default='18577297', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='place_keyword',
            field=models.CharField(default='카카오 스페이스닷원', max_length=100),
        ),
    ]
