# Generated by Django 3.2.12 on 2022-03-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220305_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='hn_id',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
