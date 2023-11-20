from django.shortcuts import render

# Create your views here.
def task_manager(request):
    titulo = "AgriTech"
    return(render(request, 'task_manager.html',  { 'titulo': titulo,
                                            'width': 'w-20',
                                            'app_1': 'Gráficas',
                                            'app_2': 'Novedades',
                                            'app_3': 'Tareas',
                                            'app_4': 'Notificaciones',
                                            'app_5': 'Ingresar',
     }))