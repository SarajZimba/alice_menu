# Generated by Django 4.0.6 on 2024-07-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_thumbnail_alter_menu_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image_bytes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
