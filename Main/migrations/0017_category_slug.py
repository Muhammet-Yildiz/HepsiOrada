# Generated by Django 3.1.4 on 2021-03-02 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0016_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
