# Generated by Django 3.1.4 on 2021-02-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_auto_20210227_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='advantage',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='oldprice',
            field=models.CharField(default='..  TL ', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default='..   TL', max_length=20),
        ),
    ]