# Generated by Django 5.1.4 on 2025-03-19 05:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Detectoy', '0028_alter_erro_momento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erro',
            name='momento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
