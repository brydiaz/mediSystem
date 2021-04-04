from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'index.html')

def crearPaciente(request):

    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PacienteForm()
    return render(request, 'appMediSystem/crearPaciente.html', {'form':form})

def listarPaciente(request):
    paciente = Paciente.objects.all()
    context = {'paciente':paciente}
    return render(request, 'appMediSystem/listarPaciente.html', context)

def editarPaciente(request, id):
    paciente = Paciente.objects.get(idPaciente=id)
    if request.method == 'GET':
        form = PacienteForm(instance = paciente)
    else:
        form = PacienteForm(request.POST, instance= paciente)
        if form.is_valid():
            form.save() 
        return redirect('index')
    return render(request, 'appMediSystem/crearPaciente.html', {'form':form})

def borrarPaciente(request, id):
    paciente = Paciente.objects.get(idPaciente=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('index')
    return render(request, 'appMediSystem/borrarPaciente.html', {'paciente':paciente})

def crearCita(request):

    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarCita')
    else:
        form = CitaForm()
    return render(request, 'appMediSystem/crearCita.html', {'form':form})

def listarCita(request):
    cita = Cita.objects.all()
    context = {'cita':cita}
    return render(request, 'appMediSystem/listarCita.html', context)

def editarCita(request, id):
    cita = Cita.objects.get(idCita=id)
    if request.method == 'GET':
        form = CitaForm(instance = cita)
    else:
        form = CitaForm(request.POST, instance= cita)
        if form.is_valid():
            form.save() 
        return redirect('listarCita')
    return render(request, 'appMediSystem/crearCita.html', {'form':form})

def borrarCita(request, id):
    cita = Cita.objects.get(idCita=id)
    if request.method == 'POST':
        cita.delete()
        return redirect('index')
    return render(request, 'appMediSystem/borrarCita.html', {'Cita':cita})


def crearDoctor(request):

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarDoctor')
    else:
        form = DoctorForm()
    return render(request, 'appMediSystem/crearDoctor.html', {'form':form})

def listarDoctor(request):
    doctor = Doctor.objects.all()
    context = {'doctor':doctor}
    return render(request, 'appMediSystem/listarDoctor.html', context)

def editarDoctor(request, id):
    doctor = Doctor.objects.get(idDoctor=id)
    if request.method == 'GET':
        form = DoctorForm(instance = doctor)
    else:
        form = DoctorForm(request.POST, instance= doctor)
        if form.is_valid():
            form.save() 
        return redirect('listarDoctor')
    return render(request, 'appMediSystem/crearDoctor.html', {'form':form})

def borrarDoctor(request, id):
    doctor = Doctor.objects.get(idDoctor=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('index')
    return render(request, 'appMediSystem/borrarDoctor.html', {'Doctor':doctor})  

def listarCitasDoctor(request, id):
    citasDoctor = Doctor.objects.get(idDoctor = id)
    citas = citasDoctor.citasPorDoctor
    context = {'citas':citas.all()}
    return render(request, 'appMediSystem/listarCitasDoctor.html', context)
     
#CRUD MONGO

def crearEbais(request):

    if request.method == 'POST':
        form = EbaisForm(request.POST)
        if form.is_valid():
            selectedObject = form.save(commit=False)
            selectedObject.save(using='mongo')
            return redirect('index')
    else:
        form = EbaisForm()
    return render(request, 'appMediSystem/crearEbais.html', {'form':form})

def listarEbais(request):
    ebais = Ebais.objects.using('mongo').all()
    context = {'ebais':ebais}
    return render(request, 'appMediSystem/listarEbais.html', context)

def borrarEbais(request, id):
    ebais = Ebais.objects.using('mongo').get(id=id)
    if request.method == 'POST':
        ebais.delete()
        return redirect('index')
    return render(request, 'appMediSystem/borrarEbais.html', {'ebais':ebais})  

def editarEbais(request, id):
    ebais = Ebais.objects.using('mongo').get(id=id)
    if request.method == 'GET':
        form = EbaisForm(instance = ebais)
    else:
        form = EbaisForm(request.POST, instance= ebais)
        if form.is_valid():
            selectedObject = form.save(commit=False)
            selectedObject.save(using='mongo')
        return redirect('listarEbais')
    return render(request, 'appMediSystem/crearEbais.html', {'form':form})


def desarrolladores(request):
    return render(request, 'appMediSystem/desarrolladores.html')