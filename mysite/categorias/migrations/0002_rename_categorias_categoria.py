# Generated by Django 4.1.5 on 2023-01-31 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categorias',
            new_name='Categoria',
        ),
    ]
