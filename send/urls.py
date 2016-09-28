from django.conf.urls import url , include
from .views import Formulario,Enviar
urlpatterns = [
    url(r'^formulario/', Formulario ),
    url(r'^enviar/', Enviar),

]
