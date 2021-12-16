# Generated by Django 2.2.4 on 2021-12-10 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField(default='Sua mensagem')),
                ('estadoVisto', models.BooleanField(default=False)),
                ('dataEnvio', models.DateTimeField(auto_now_add=True)),
                ('receptor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recebe_mensagem', to=settings.AUTH_USER_MODEL)),
                ('transmissor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='envia_mensagem', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('dataEnvio',),
            },
        ),
    ]