# Generated by Django 3.2.9 on 2021-12-27 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_hostingplace_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostingplace',
            name='user',
        ),
        migrations.AddField(
            model_name='hostingplace',
            name='username',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
