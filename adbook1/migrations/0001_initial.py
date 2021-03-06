# Generated by Django 3.1.7 on 2021-03-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('surname', models.CharField(max_length=255, unique=True)),
                ('address_country', models.CharField(blank=True, max_length=255)),
                ('address_sity', models.CharField(blank=True, max_length=255)),
                ('address_street', models.CharField(blank=True, max_length=255)),
                ('url', models.URLField(blank=True, max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=255)),
                ('img_user', models.ImageField(blank=True, max_length=255, null=True, upload_to='static/images/')),
            ],
        ),
    ]
