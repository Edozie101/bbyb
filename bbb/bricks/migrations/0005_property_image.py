# Generated by Django 2.1.7 on 2019-04-17 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bricks', '0004_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(default='images/logo.png', upload_to=''),
        ),
    ]
