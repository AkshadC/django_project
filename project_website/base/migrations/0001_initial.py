# Generated by Django 4.2.17 on 2025-01-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=50, verbose_name='a')),
                ('b', models.CharField(max_length=50, verbose_name='b')),
                ('c', models.CharField(max_length=50, verbose_name='c')),
                ('d', models.CharField(max_length=50, verbose_name='d')),
            ],
        ),
    ]
