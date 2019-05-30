from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def paciente_list(request):
    return render(request, 'paciente/list.html')

def paciente_show(request, paciente_id):
    return render(request, 'paciente/show.html', {'paciente_id':paciente_id})

def medico_list(request):
    return render(request, 'medico/list.html')

def medico_show(request, medico_id):
    return render(request, 'medico/show.html', {'medico_id':medico_id})   

def agendamento_list (request):
    return render(request, 'agendamento/list.html')    


   
   
 

