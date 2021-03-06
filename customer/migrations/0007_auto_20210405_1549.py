# Generated by Django 3.1.4 on 2021-04-05 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20210403_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Dogum Tarihi'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'erkek'), ('female', 'kadın')], max_length=50, verbose_name='Cinsiyet'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Cep Telefonu'),
        ),
    ]
