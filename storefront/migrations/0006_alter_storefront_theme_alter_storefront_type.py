# Generated by Django 4.1.3 on 2022-12-13 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0005_alter_storefront_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storefront',
            name='theme',
            field=models.CharField(choices=[('theme1', 'theme1'), ('theme2', 'theme2'), ('theme3', 'theme3')], default='theme1', max_length=100),
        ),
        migrations.AlterField(
            model_name='storefront',
            name='type',
            field=models.CharField(choices=[('business', 'business'), ('shop', 'shop')], default='shop', max_length=100),
        ),
    ]