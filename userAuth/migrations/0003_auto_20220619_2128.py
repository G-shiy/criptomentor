# Generated by Django 3.2.12 on 2022-06-19 21:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0002_alter_usuario_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=60)),
                ('imagem', models.ImageField(upload_to='')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('video', models.URLField()),
                ('theme', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=25)),
                ('time', models.CharField(blank=True, choices=[('01', '5'), ('02', '10'), ('03', '15'), ('04', '20')], max_length=3)),
                ('imagem', models.ImageField(upload_to='')),
                ('thumbnail', models.ImageField(blank=True, upload_to='')),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('video', models.URLField()),
                ('theme', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='text',
            name='types',
        ),
        migrations.AlterField(
            model_name='text',
            name='theme',
            field=models.CharField(max_length=60),
        ),
    ]
