# Generated by Django 3.0.5 on 2021-04-03 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMediSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('idCita', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCita', models.DateField()),
                ('motivoCita', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('pesoPaciente', models.CharField(max_length=100)),
                ('generoPaciente', models.CharField(max_length=100)),
                ('nombrePaciente', models.CharField(max_length=100)),
                ('tipoDeSangrePaciente', models.CharField(max_length=100)),
                ('cedulaPaciente', models.CharField(max_length=100)),
                ('edadPaciente', models.IntegerField()),
                ('alturaPaciente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('idDoctor', models.AutoField(primary_key=True, serialize=False)),
                ('especialidadDoctor', models.CharField(max_length=200)),
                ('nombreDoctor', models.CharField(max_length=100)),
                ('citasPorDoctor', models.ManyToManyField(to='appMediSystem.Cita')),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='pacienteFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMediSystem.Paciente'),
        ),
    ]
