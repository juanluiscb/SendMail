# encoding:utf-8
from django.shortcuts import render
from django.template.context_processors import csrf
from django.conf import settings
from django.core.mail import send_mail
import sys


reload(sys)
sys.setdefaultencoding("utf-8")

#de la configuración traemos el correo para enviar
envia = settings.DEFAULT_FROM_EMAIL

contexto = {
  'title' : ':: Enviar Correos',
  'conteido': 'Enviar Correos',
}

def Formulario(request):
  contexto.update(csrf(request))
  return render(request,'send_mail.html',contexto)

def Enviar(request):
  if request.method == 'POST':
    contexto [ 'contenido' ] = 'Preparando para enviar'
    destinatario = (''+request.POST['destino']+'',)
    subject = request.POST['subject']
    mensaje = request.POST['mensaje']
    send_mail(subject,mensaje,envia,destinatario,fail_silently=False)
  else:
    contexto [ 'contenido' ] = 'No hay información válida'

  return render(request,'base.html',contexto)