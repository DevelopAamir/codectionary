# Generated by Django 4.1.5 on 2023-01-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codectionaryapp', '0015_alter_content_creator_alter_creator_channel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='likes',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
