# Generated by Django 4.2.9 on 2024-02-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='img')),
                ('description', models.TextField()),
            ],
        ),
    ]
