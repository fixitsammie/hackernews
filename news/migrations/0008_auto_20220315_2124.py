# Generated by Django 3.2.12 on 2022-03-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_story_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='score',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='time',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='story',
            name='type',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
