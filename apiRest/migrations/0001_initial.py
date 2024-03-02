# Generated by Django 5.0.2 on 2024-03-02 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('grado', models.CharField(max_length=45)),
                ('seccion', models.CharField(max_length=2)),
                ('edad', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
