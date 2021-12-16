# Generated by Django 2.2.4 on 2021-08-23 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0006_auto_20210808_1327'),
        ('estudante', '0006_auto_20210822_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliarProfessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.IntegerField()),
                ('dataRegisto', models.DateTimeField(auto_now_add=True)),
                ('eEstudante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estudante.Estudante')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='professor.Professor')),
            ],
        ),
    ]