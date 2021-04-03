from django.db import models

# Create your models here.
class Ebais(models.Model):

    idEbais = models.AutoField(primary_key=True)
    nombreEbais = models.CharField(max_length=100)
    ubicacionEbais = models.CharField(max_length=300)
    capacidadEbais = models.IntegerField()


class Paciente(models.Model):

    idPaciente = models.AutoField(primary_key= True)
    pesoPaciente = models.CharField(max_length=100)
    generoPaciente = models.CharField(max_length=100)
    nombrePaciente = models.CharField(max_length=100)
    tipoDeSangrePaciente = models.CharField(max_length=100)
    cedulaPaciente = models.CharField(max_length=100)
    edadPaciente = models.IntegerField()
    alturaPaciente = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.cedulaPaciente)
         

class Cita(models.Model):

    idCita = models.AutoField(primary_key=True)
    fechaCita = models.DateField()
    motivoCita = models.CharField(max_length=200)
    pacienteFK = models.ForeignKey(Paciente, on_delete= models.CASCADE)

    def __str__(self):
        return '{}'.format(str(self.fechaCita) + " ASOCIADA A "+ self.pacienteFK.cedulaPaciente+" POR "+ self.motivoCita)



class Doctor(models.Model):

    idDoctor = models.AutoField(primary_key=True)
    especialidadDoctor = models.CharField(max_length=200)
    nombreDoctor = models.CharField(max_length=100)
    citasPorDoctor = models.ManyToManyField(Cita)

class Ebais(models.Model):

    nombreEbais = models.CharField(max_length=100)
    ubicacionEbais = models.CharField(max_length=300)
    capacidadEbais = models.IntegerField()

