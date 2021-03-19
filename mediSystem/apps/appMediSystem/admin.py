from django.contrib import admin
from .models import Paciente, Cita, Doctor

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Cita)
admin.site.register(Doctor)