# Generated by Django 2.2.4 on 2021-09-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0006_auto_20210808_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
