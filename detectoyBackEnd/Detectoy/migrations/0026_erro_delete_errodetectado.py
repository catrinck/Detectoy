# Generated by Django 5.1.4 on 2025-03-18 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Detectoy', '0025_alter_errodetectado_imagem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Erro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField(default=datetime.datetime(2025, 3, 18, 19, 40, 58, 77858, tzinfo=datetime.timezone.utc))),
                ('linha', models.IntegerField(choices=[(0, 'Linha 1'), (1, 'Linha 2'), (2, 'Linha 3')])),
                ('tipo', models.IntegerField(choices=[(0, 'Preta'), (1, 'Branca')])),
                ('tela_quebrada', models.BooleanField()),
                ('carcaca_quebrada', models.BooleanField()),
                ('imagem', models.FilePathField(path='/home/pedroituassu/projects/Detectoy/detectoyBackEnd/Detectoy/images')),
            ],
        ),
        migrations.DeleteModel(
            name='ErroDetectado',
        ),
    ]
