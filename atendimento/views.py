from django.shortcuts import render
from . models import Paciente
from . models import Medico
from . models import Medicamento

def home(request):
    return render(request, 'home.html')

def paciente_list(request):
    pacientes=Paciente.objects.all()
    return render(request, 'paciente/list.html', {'pacientes': pacientes})

def paciente_show(request, paciente_id):
    return render(request, 'paciente/show.html', {'paciente_id':paciente_id})

def medico_list(request):
    medicos=Medico.objects.all()
    return render(request, 'medico/list.html', {'medicos': medicos})

def medico_show(request, medico_id):
    return render(request, 'medico/show.html', {'medico_id':medico_id})   

def agendamento_list (request):
    return render(request, 'agendamento/list.html')  

def medicamento_list(request):
    medicamentos=Medicamento.objects.all()
    return render(request, 'medicamento/list.html', {'medicamentos': medicamentos})
    


   
   
 

