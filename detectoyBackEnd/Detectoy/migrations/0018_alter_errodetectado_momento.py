# Generated by Django 5.1.4 on 2025-02-13 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Detectoy', '0017_alter_errodetectado_momento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errodetectado',
            name='momento',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 13, 15, 45, 34, 707828, tzinfo=datetime.timezone.utc)),
        ),
    ]
