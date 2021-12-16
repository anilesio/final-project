# Generated by Django 2.2.4 on 2021-10-02 15:46

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
            name='CategoriaMagazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=50)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('estado', models.BooleanField(default=True)),
                ('usuario', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReportarErro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_erro', models.CharField(choices=[('Anúncios', 'Anúncios'), ('Mensagens', 'Mensagens'), ('Upload de fotos', 'Upload de fotos'), ('Meu perfil', 'Meu perfil'), ('Central de ajuda', 'Central de ajuda')], max_length=40)),
                ('mensagem', models.TextField()),
                ('anexo_foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('usuario', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(blank=True, choices=[('Em espera', 'Em espera'), ('Visto', 'Visto'), ('Resolvido', 'Resolvido'), ('Ignorar', 'Ignorar')], default='Em espera', max_length=30, null=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoArtigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('icone', models.ImageField(blank=True, default='noticia_default.png', upload_to='')),
                ('usuario', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoErro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('usuario', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mensagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receptor', models.CharField(blank=True, max_length=100, null=True)),
                ('mensagem', models.TextField()),
                ('data_registo', models.DateTimeField(auto_now_add=True)),
                ('emissor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importancia', models.CharField(blank=True, choices=[('Destaque', 'Destaque'), ('Normal', 'Normal')], default='Normal', max_length=30, null=True)),
                ('estado', models.CharField(blank=True, choices=[('Activado', 'Activado'), ('Desactivado', 'Desactivado')], default='Activado', max_length=30, null=True)),
                ('titulo_magazine', models.CharField(max_length=100)),
                ('corpo_magazine', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('foto', models.ImageField(blank=True, default='noticia_default.png', upload_to='')),
                ('usuario', models.CharField(blank=True, max_length=200, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestaoInterna.CategoriaMagazine')),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.CharField(blank=True, max_length=200, null=True)),
                ('tipo_artigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestaoInterna.TipoArtigo')),
            ],
        ),
    ]
