# Generated by Django 4.1.5 on 2023-01-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codectionaryapp', '0003_alter_creator_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='zip_code',
            field=models.IntegerField(default=0),
        ),
    ]
