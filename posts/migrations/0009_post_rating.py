# Generated by Django 3.2.18 on 2023-04-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_rename_category_post_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]