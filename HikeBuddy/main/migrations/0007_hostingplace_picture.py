# Generated by Django 3.2.9 on 2021-12-23 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_hostingplace_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostingplace',
            name='picture',
            field=models.ImageField(blank=True, upload_to='static\\media\\host_pics'),
        ),
    ]
