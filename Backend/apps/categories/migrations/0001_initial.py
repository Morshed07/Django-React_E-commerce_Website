# Generated by Django 5.0.3 on 2024-03-05 18:53

import autoslug.fields
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
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-id'],
            },
        ),
    ]
