# Generated by Django 4.2.2 on 2023-08-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_details_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='email_id',
            field=models.EmailField(max_length=254, verbose_name='mno@gmail.com'),
        ),
    ]
