# Generated by Django 5.0 on 2024-01-01 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgcontactinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='orginfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='orglocation',
            name='id',
        ),
        migrations.AlterField(
            model_name='orgcontactinfo',
            name='org',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orginfo',
            name='org',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orglocation',
            name='org',
            field=models.OneToOneField(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
