# Generated by Django 4.1.5 on 2023-01-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codectionaryapp', '0025_saves_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='desciption',
            field=models.CharField(default='', max_length=200),
        ),
    ]
