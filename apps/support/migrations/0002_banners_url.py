# Generated by Django 2.0.8 on 2019-03-12 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banners',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
