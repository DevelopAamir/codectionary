# Generated by Django 4.1.5 on 2023-01-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codectionaryapp', '0006_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='content',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]