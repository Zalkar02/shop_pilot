# Generated by Django 3.0.4 on 2020-04-01 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200401_1427'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImage',
            new_name='ProductItemImage',
        ),
    ]
