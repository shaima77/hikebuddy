# Generated by Django 3.2.9 on 2021-12-23 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_auto_20211129_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostingPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('fireplace', models.BooleanField()),
                ('singleBeds', models.BooleanField()),
                ('doubleBeds', models.BooleanField()),
                ('freeWiFi', models.BooleanField()),
                ('showers', models.BooleanField()),
                ('electricity', models.BooleanField()),
                ('breakfast', models.BooleanField()),
                ('airConditioning', models.BooleanField()),
                ('parking', models.BooleanField()),
                ('bar', models.BooleanField()),
                ('picture', models.ImageField(blank=True, upload_to='static\\media\\host_pics')),
            ],
        ),
    ]
