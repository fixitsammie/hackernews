# Generated by Django 3.2.12 on 2022-03-05 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_story_hn_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='hacker_news_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 5, 15, 25, 3, 704107)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='hn_id',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='hn_parent',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='kids',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
