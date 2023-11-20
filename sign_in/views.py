from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def sign_in(request):
    titulo = "AgriTech"
    return(render(request, 'sign_in.html',  { 'titulo': titulo,
                                            'width': 'w-20',
                                            'app_1': 'Gráficas',
                                            'app_2': 'Novedades',
                                            'app_3': 'Tareas',
                                            'app_4': 'Notificaciones',
                                            'app_5': 'Ingresar',
     }))