# Generated by Django 3.2.3 on 2021-06-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.URLField(blank=True),
        ),
    ]
