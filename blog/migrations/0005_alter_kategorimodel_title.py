# Generated by Django 3.2.7 on 2021-12-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211201_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorimodel',
            name='title',
            field=models.CharField(blank=True, max_length=50, unique=True, verbose_name='Kategori'),
        ),
    ]
