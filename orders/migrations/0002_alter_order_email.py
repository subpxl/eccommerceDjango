# Generated by Django 4.1.3 on 2022-12-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]