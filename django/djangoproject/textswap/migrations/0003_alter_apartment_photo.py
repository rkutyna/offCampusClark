# Generated by Django 5.0.1 on 2024-04-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textswap', '0002_message_time_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='photo',
            field=models.ImageField(upload_to='textswap/static/images'),
        ),
    ]