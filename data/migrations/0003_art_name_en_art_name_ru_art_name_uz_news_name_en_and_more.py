# Generated by Django 4.2.1 on 2023-05-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='art',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='art',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='news',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='news',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='news',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.TextField(null=True, verbose_name='Matn'),
        ),
    ]
