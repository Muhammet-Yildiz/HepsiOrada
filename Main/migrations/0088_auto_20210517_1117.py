# Generated by Django 3.1.4 on 2021-05-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0087_auto_20210510_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_imgs/', verbose_name='Ürün Fotografları '),
        ),
    ]
