# Generated by Django 3.1.4 on 2021-04-03 16:58

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_remove_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('erkek', 'male'), ('kadın', 'female')], max_length=50, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]