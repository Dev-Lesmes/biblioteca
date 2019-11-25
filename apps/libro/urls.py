from django.urls import path, re_path
from .views import crearAutor, listarAutor, editarAutor,eliminarAutor

urlpatterns = [
    # path recibe: ruta url / función de la vista / nombre de la ruta
    # path es la manera que se usa en django 2.0
    path('crear_autor/', crearAutor, name='crear_autor'),
    path('listar_autor/', listarAutor, name='listar_autor'),
    path('editar_autor/<int:id>', editarAutor, name='editar_autor'),
    path('eliminar_autor/<int:id>',eliminarAutor, name='eliminar_autor')

    # re_path trabaja con la libreria de regex
    #re_path(r'^crear_autor/(?P<id>\d+)',crearAutor, name = "crear_autor")
    # antiguamente se usaba url() para la versiones viejas de django
]
