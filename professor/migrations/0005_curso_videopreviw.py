# Generated by Django 2.2.4 on 2021-08-08 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0004_curso_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='videoPreviw',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]