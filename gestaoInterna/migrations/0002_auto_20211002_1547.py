# Generated by Django 2.2.4 on 2021-10-02 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestaoInterna', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artigo',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='categoriamagazine',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='reportarerro',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='tipoartigo',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='tipoerro',
            name='usuario',
        ),
        migrations.AddField(
            model_name='artigo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categoriamagazine',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='magazine',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reportarerro',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tipoartigo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tipoerro',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
