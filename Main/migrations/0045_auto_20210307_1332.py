# Generated by Django 3.1.4 on 2021-03-07 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0044_auto_20210307_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='indirim',
        ),
        migrations.AddField(
            model_name='product',
            name='indirsim',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Main.i̇ndirim'),
            preserve_default=False,
        ),
    ]
