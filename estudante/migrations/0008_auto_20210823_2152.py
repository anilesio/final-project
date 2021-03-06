# Generated by Django 2.2.4 on 2021-08-23 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estudante', '0007_avaliarprofessor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliarprofessor',
            name='eEstudante',
        ),
        migrations.AddField(
            model_name='avaliarprofessor',
            name='estudante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='estudante_avaliacao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='avaliarprofessor',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professor_avaliacao', to=settings.AUTH_USER_MODEL),
        ),
    ]
