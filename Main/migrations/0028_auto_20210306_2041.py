# Generated by Django 3.1.4 on 2021-03-06 17:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0027_auto_20210306_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='heart',
        ),
        migrations.AddField(
            model_name='product',
            name='heart',
            field=models.ManyToManyField(related_name='Begenenler', to=settings.AUTH_USER_MODEL),
        ),
    ]
