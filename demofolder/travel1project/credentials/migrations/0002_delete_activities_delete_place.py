# Generated by Django 4.2.9 on 2024-02-11 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Activities',
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]
