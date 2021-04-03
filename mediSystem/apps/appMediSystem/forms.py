from django import forms
from .models import *
import datetime


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente  
        fields = [
            'idPaciente',
            'pesoPaciente',
            'generoPaciente',
            'nombrePaciente',
            'tipoDeSangrePaciente',
            'cedulaPaciente',
            'edadPaciente',
            'alturaPaciente'
        ]

        labels = {

            'idPaciente':'ID',
            'pesoPaciente':'Peso',
            'generoPaciente':'Genero',
            'nombrePaciente':'Nombre',
            'tipoDeSangrePaciente':'Tipo de Sangre',
            'cedulaPaciente':'Cedula',
            'edadPaciente':'Edad',
            'alturaPaciente':'Altura'

        }

        widgets =   {
  
            'idPaciente': forms.TextInput(attrs={'class':'form-control'}),
            'pesoPaciente': forms.TextInput(attrs={'class':'form-control'}),
            'generoPaciente': forms.TextInput(attrs={'class':'form-control'}),
            'nombrePaciente': forms.TextInput(attrs={'class':'form-control'}),
            'tipoDeSangrePaciente': forms.TextInput(attrs={'class':'form-control'}),
            'cedulaPaciente': forms.TextInput(attrs={'class':'form-control'}),
            'edadPaciente': forms.TextInput(attrs={'class':'form-control'}),
            'alturaPaciente': forms.TextInput(attrs={'class':'form-control'})

        }

class CitaForm(forms.ModelForm):

    class Meta:
        model = Cita  
        fields = {
            'idCita',
            'fechaCita',
            'motivoCita',
            'pacienteFK'
        }
        labels ={

            'idCita':'ID',
            'fechaCita':'Fecha',
            'motivoCita':'Motivo',
            'pacienteFK':'Paciente Asociado'

        }

        widgets = {

            'idCita': forms.TextInput(attrs={'class':'form-control'}),
            'fechaCita': forms.DateInput(format='%d/%m/%Y' ),
            'motivoCita': forms.TextInput(attrs={'class':'form-control'}),
            'pacienteFK':forms.Select()
        }

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor  
        fields = {
            'idDoctor',
            'especialidadDoctor',
            'nombreDoctor',
            'citasPorDoctor'
        }

        labels = {

            'idDoctor':'ID',
            'especialidadDoctor':'Especialidad',
            'nombreDoctor':'Nombre',
            'citasPorDoctor':'Asignación de citas'

        }

        widgets = {

            'idDoctor': forms.TextInput(attrs={'class':'form-control'}) ,
            'especialidadDoctor': forms.TextInput(attrs={'class':'form-control'}),
            'nombreDoctor': forms.TextInput(attrs={'class':'form-control'}),
            'citasPorDoctor': forms.CheckboxSelectMultiple()

        }


class EbaisForm(forms.ModelForm):

    class Meta:
        model = Ebais  
        fields = {
            'id',
            'nombreEbais',
            'ubicacionEbais',
            'capacidadEbais'
        } 

        labels = {

            'id':'ID',
            'nombreEbais':'Nombre',
            'ubicacionEbais':'Ubicación',
            'capacidadEbais':'Capacidad de Personas'

        }

        widgets = {

            'id': forms.TextInput(attrs={'class':'form-control'}) ,
            'nombreEbais': forms.TextInput(attrs={'class':'form-control'}),
            'ubicacionEbais': forms.TextInput(attrs={'class':'form-control'}),
            'capacidadEbais': forms.TextInput(attrs={'class':'form-control'}),

        }
