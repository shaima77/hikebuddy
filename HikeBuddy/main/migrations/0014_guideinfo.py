# Generated by Django 3.2.9 on 2021-12-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_hostingplace_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=200)),
                ('carryweapon', models.BooleanField(default=False)),
                ('medic', models.BooleanField(default=False)),
                ('transportationvehicle', models.BooleanField(default=False)),
                ('username', models.CharField(default='', max_length=200)),
            ],
        ),
    ]