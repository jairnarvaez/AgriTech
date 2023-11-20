from django.shortcuts import render

# Create your views here.

def news(request):
    titulo = "AgriTech"
    historia = '''
                Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.
               '''

    trabajos = '''
                Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.
                '''

    estacion = '''
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam lacinia malesuada bibendum. Aliquam quis tortor in massa lobortis sagittis. Aliquam nisi augue, egestas ut magna nec, interdum auctor elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Praesent porta luctus diam, non pulvinar diam semper nec. Nulla sed sollicitudin urna. Aliquam gravida facilisis libero id gravida. Donec at maximus neque. Integer lorem est, scelerisque quis tempor id, pellentesque ut ipsum. Cras lobortis ac sem at auctor. Cras sed est convallis, porta massa nec, rutrum velit. Aliquam id lacinia mauris, vel iaculis lacus. Aliquam ac nisl posuere, pretium ipsum nec, porta nisi. In vel sem ac lectus pretium cursus at et risus. Aenean vestibulum magna sem. Etiam aliquet ullamcorper tempus. Nam venenatis iaculis ex, vestibulum lacinia arcu dignissim vitae. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam luctus auctor nibh, nec tempor lectus laoreet nec. Aliquam dignissim consectetur felis non lobortis. Phasellus sed neque tempor, lobortis ipsum a, porta metus. Sed interdum vel tortor sed fermentum. Sed at tristique est. Aenean vulputate auctor sem, eget blandit nisi condimentum sit amet. Maecenas ut risus ut erat consequat convallis. Duis eget risus aliquet, tincidunt risus ut, commodo est. 
               '''

    return(render(request, 'news.html',  { 'titulo': titulo,
                                            'width': 'w-20',
                                            'app_1': 'Gráficas',
                                            'app_2': 'Novedades',
                                            'app_3': 'Tareas',
                                            'app_4': 'Notificaciones',
                                            'app_5': 'Ingresar',
                                            'historia': historia,
                                            'trabajos': trabajos,
                                            'estacion': estacion
     }))