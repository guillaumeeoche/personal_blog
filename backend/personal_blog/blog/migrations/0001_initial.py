# Generated by Django 4.1.6 on 2023-06-03 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('category', models.CharField(choices=[('world', 'World'), ('environment', 'Environment'), ('it', 'It'), ('design', 'Design'), ('life', 'Life'), ('travel', 'Travel'), ('linkedin', 'Linkedin')], default='world', max_length=50)),
                ('thumbmail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('excerpt', models.CharField(max_length=150)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('content', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
