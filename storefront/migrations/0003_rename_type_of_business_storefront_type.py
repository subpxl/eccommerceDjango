# Generated by Django 4.1.3 on 2022-12-13 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0002_storefront_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storefront',
            old_name='type_of_business',
            new_name='type',
        ),
    ]
