# Generated by Django 3.2.7 on 2021-10-15 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211014_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tessiu',
            options={'verbose_name': 'Tejido', 'verbose_name_plural': 'Tejidos'},
        ),
        migrations.AddField(
            model_name='tessiu',
            name='color',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
