# Generated by Django 4.2.4 on 2023-12-04 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_item_units_description_item_want'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]
