# Generated by Django 5.0.3 on 2024-03-05 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name_plural': 'Products'},
        ),
    ]
