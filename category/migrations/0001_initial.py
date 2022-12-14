# Generated by Django 4.1.1 on 2022-10-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
