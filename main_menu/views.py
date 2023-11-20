from django.shortcuts import render
from django.http.response import JsonResponse
from .models import DataBaseHumidity, DataBaseNutrients, DataBaseTemperature, DataBasePhosphorus
from datetime import datetime, timedelta
from random import randint
import random


# Create your views here.
def main_menu(request):
    titulo = "AgriTech"

    return render(request, 'index.html', { 'titulo': titulo,
                                            'width': 'w-20',
                                            'app_1': 'Gráficas',
                                            'app_2': 'Novedades',
                                            'app_3': 'Tareas',
                                            'app_4': 'Notificaciones',
                                            'app_5': 'Ingresar',
     })

# Guardar en la base de datos (solo pruebas)
def set_chart():
    date = datetime.datetime.now()
    hora_actual = date.hour + 5
    minuto_actual = date.second 
    date = str(hora_actual) +':' + str(minuto_actual) 
    d = DataBaseTemperature(data_date=date, data_value=randint(10,100))
    d.save()

def read_data_base_humidity():
    datos = DataBaseHumidity.objects.all()
    data_value = []
    data_date = []

    for dato in datos:
      data_value.append(dato.data_value)
      data_date.append(dato.data_date)

    return data_date, data_value

def read_data_base_nutrients():
    datos = DataBaseNutrients.objects.all()
    data_value = []
    data_date = []

    for dato in datos:
      data_value.append(dato.data_value)
      data_date.append(dato.data_date)

    return data_date, data_value

def read_data_base_temperature():
    datos = DataBaseTemperature.objects.all()
    data_value = []
    data_date = []

    for dato in datos:
      data_value.append(dato.data_value)
      data_date.append(dato.data_date)

    return data_date, data_value

def read_data_base_phosphorus():
    datos = DataBasePhosphorus.objects.all()
    data_value = []
    data_date = []

    for dato in datos:
      data_value.append(dato.data_value)
      data_date.append(dato.data_date)

    return data_date, data_value

def get_graph_humidity(request):
    data = []
    date, value = read_data_base_humidity()

    for i in range(0, len(date)-1):
        data.append([date[i], value[i]])

    chart = {
        'tooltip': {
            'trigger': 'axis'
        },
        'legend': {
            'top': 'bottom',
            'left': 0
        },
        'toolbox': {
            'top': 'bottom',
            'show': 'true',
            'feature': {
            'dataZoom': {
                'yAxisIndex': 'none'
            },
            'dataView': { 'readOnly': 'false' },
            'magicType': { 'type': ['line', 'bar'] },
            'restore': {},
            'saveAsImage': {}
            }
        },
        'xAxis': {
            'type': 'category',
            'boundaryGap': 'false',
            'data': date
        },
        'yAxis': {
            'type': 'value',
            'axisLabel': {
            'formatter': '{value} %'
            }
        },

       # 'dataZoom': [
        #        {
         #       'type': 'inside',
          #      'start': 60,
           #     'end': 100
            #    },
             #   {
              #  'start': 60,
               # 'end': 100
               # }
               # ],
        'series': [

            {
            'name': 'Lowest',
            'type': 'line',
            'color': '#47a0f0',
            'data': value,
            'smooth': 'true',
            'markLine': {
                'data': [
                { 'type': 'average', 'name': 'Avg' },
                [
                    {
                    'symbol': 'none',
                    'x': '90%',
                    'yAxis': 'max'
                    },

                    {
                    'symbol': 'circle',
                    'label': {
                        'position': 'start',
                        'formatter': 'Max'
                    },
                    'type': 'max',
                    'name': '最高点'
                    }
                ]
                ]
            }
            }
        ]
    }
    return JsonResponse(chart)

def get_graph_nutrients(request):
    data = []
    date, value = read_data_base_nutrients()

    for i in range(0, len(date)-1):
        data.append([date[i], value[i]])

    chart =  {
        'tooltip': {
            'trigger': 'axis'
        },
        'legend': {
            'top': 'bottom',
            'left': 0
        },

        'toolbox': {
            'top': 'bottom',
            'show': 'true',
            'feature': {
            'dataZoom': {
                'yAxisIndex': 'none'
            },
            'dataView': { 'readOnly': 'false' },
            'magicType': { 'type': ['line', 'bar'] },
            'restore': {},
            'saveAsImage': {}
            }
        },
        'xAxis': {
            'type': 'category',
            'data': date
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [
            {
            'data': value,
            'type': 'line',
            'smooth': 'true',
            'color': '#6f9459',
            }
        ]
    }
    return JsonResponse(chart)

def get_graph_temperature(request):
    data = []
    date, value = read_data_base_temperature()

    for i in range(0, len(date)-1):
        data.append([date[i], value[i]])

    chart = {
        'tooltip': {
            'trigger': 'axis'
        },
        'legend': {
            'top': 'bottom',
            'left': 0
        },

        'toolbox': {
            'top': 'bottom',
            'show': 'true',
            'feature': {
            'dataZoom': {
                'yAxisIndex': 'none'
            },
            'dataView': { 'readOnly': 'false' },
            'magicType': { 'type': ['line', 'bar'] },
            'restore': {},
            'saveAsImage': {}
            }
        },
        'xAxis': {
            'type': 'category',
            'boundaryGap': 'false',
            'data': date
        },
        'yAxis': {
            'type': 'value',
            'axisLabel': {
            'formatter': '{value} °C'
            }
        },
        'series': [
            {
            'name': 'Lowest',
            'type': 'line',
            'color': '#ee6666',
            'smooth': 'true',
            'data': value,
           # 'markPoint': {
            #    'data': [{ 'name': '周最低', 'value': -2, 'xAxis': 1, 'yAxis': -1.5 }]
            #},
            'markLine': {
                'data': [
                { 'type': 'average', 'name': 'Avg' },
                [
                    {
                    'symbol': 'none',
                    'x': '90%',
                    'yAxis': 'max'
                    },
                    {
                    'symbol': 'circle',
                    'label': {
                        'position': 'start',
                        'formatter': 'Max'
                    },
                    'type': 'max',
                    'name': '最高点'
                    }
                ]
                ]
            }
            }
        ]
    }
    return JsonResponse(chart)

def get_graph_phosphorus(request):
    data = []
    date, value = read_data_base_phosphorus()

    for i in range(0, len(date)-1):
        data.append([date[i], value[i]])

    chart = {
        'tooltip': {
            'trigger': 'axis'
        },
        'legend': {
            'top': 'bottom',
            'left': 0
        },

        'toolbox': {
            'top': 'bottom',
            'show': 'true',
            'feature': {
            'dataZoom': {
                'yAxisIndex': 'none'
            },
            'dataView': { 'readOnly': 'false' },
            'magicType': { 'type': ['line', 'bar'] },
            'restore': {},
            'saveAsImage': {}
            }
        },
        'xAxis': {
            'type': 'category',
            'boundaryGap': 'false',
            'data': date,
        },
        'yAxis': {
            'type': 'value',
            'axisLabel': {
            'formatter': '{value} mg'
            }
        },
        'series': [

            {
            'name': 'Lowest',
            'type': 'line',
            'color': '#f9c55a',
            'data': value,
            'smooth': 'true',
            #'markPoint': {
             #   'data': [{ 'name': '周最低', 'value': 3, 'xAxis': 4, 'yAxis': 3 }]
            #},
            'markLine': {
                'data': [
                { 'type': 'average', 'name': 'Avg' },
                [
                    {
                    'symbol': 'none',
                    'x': '90%',
                    'yAxis': 'max'
                    },
                    {
                    'symbol': 'circle',
                    'label': {
                        'position': 'start',
                        'formatter': 'Max'
                    },
                    'type': 'max',
                    'name': '最高点'
                    }
                ]
                ]
            }
            }
        ]
    }
    return JsonResponse(chart)

def get_graph_pie(request):
    chart = {

        'tooltip': {
            'trigger': 'item'
        },
        'legend': {
            'orient': 'vertical',
            'left': 'left',
            'top': 'bottom'
        },
        'series': [
            {
            'name': 'Access From',
            'type': 'pie',
            'radius': '50%',
            'data': [
                { 'value': 1048, 'name': 'Nutrientes' },
                { 'value': 735, 'name': 'Fósforo' },
                { 'value': 580, 'name': 'Nitrogeno' },
                { 'value': 484, 'name': 'Minerales' },
                { 'value': 300, 'name': 'Potacio' }
            ],
            'emphasis': {
                'itemStyle': {
                'shadowBlur': 10,
                'shadowOffsetX': 0,
                'shadowColor': 'rgba(0, 0, 0, 0.5)'
                }
            }
            }
        ]
    }
    return JsonResponse(chart)

def get_graph_large(request):
    colors = ['#5470C6', '#EE6666'];
    chart = {
    'color': colors,
    'tooltip': {
        'trigger': 'none',
        'axisPointer': {
        'type': 'cross'
        }
    },
    'legend': {},
    'grid': {
        'top': 70,
        'bottom': 50
    },
    'xAxis': [
        {
        'type': 'category',
        'axisTick': {
            'alignWithLabel': 'true'
        },
        'axisLine': {
            'onZero': 'false',
            'lineStyle': {
            'color': colors[1]
            }
        },

        'data': ['2016-1', '2016-2', '2016-3', '2016-4', '2016-5', '2016-6', '2016-7', '2016-8', '2016-9', '2016-10', '2016-11', '2016-12']
        },
        {
        'type': 'category',
        'axisTick': {
            'alignWithLabel': 'true'
        },
        'axisLine': {
            'onZero': 'false',
            'lineStyle': {
            'color': colors[0]
            }
        },
        'data': ['2015-1', '2015-2', '2015-3', '2015-4', '2015-5', '2015-6', '2015-7', '2015-8', '2015-9', '2015-10', '2015-11', '2015-12']
        }
    ],
    'yAxis': [
        {
        'type': 'value'
        }
    ],
    'series': [
        {
        'name': 'Precipitation(2015)',
        'type': 'line',
        'xAxisIndex': 1,
        'smooth': 'true',
        'emphasis': {
            'focus': 'series'
        },
        'data': [
            2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3
        ]
        },
        {
        'name': 'Precipitationes(2023)',
        'type': 'line',
        'smooth': 'true',
        'emphasis': {
            'focus': 'series'
        },
        'data': [
            3.9, 5.9, 11.1, 18.7, 48.3, 69.2, 231.6, 46.6, 55.4, 18.4, 10.3, 0.7
        ]
        }
    ]
    }
    return JsonResponse(chart)