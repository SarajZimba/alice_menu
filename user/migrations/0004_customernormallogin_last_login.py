# Generated by Django 4.0.6 on 2024-07-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customergooglelogin_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customernormallogin',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
