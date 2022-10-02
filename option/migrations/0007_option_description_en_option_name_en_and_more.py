# Generated by Django 4.1.1 on 2022-10-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option', '0006_alter_option_options_alter_option_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='option',
            name='name_en',
            field=models.CharField(default='', max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='option',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]