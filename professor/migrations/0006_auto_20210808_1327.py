# Generated by Django 2.2.4 on 2021-08-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0005_curso_videopreviw'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='videoPreviw',
        ),
        migrations.AddField(
            model_name='curso',
            name='videoPreview',
            field=models.FileField(blank=True, null=True, upload_to='preview/'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to='thumb/'),
        ),
    ]
