# Generated by Django 4.1.3 on 2022-12-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0007_alter_storefront_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='storefront',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
