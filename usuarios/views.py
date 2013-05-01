from django.shortcuts import render_to_response
from django.template import RequestContext
from usuarios.models import Datos
from usuarios.forms import UsuariosForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
import simplejson as json

def index(request):
	usuarios = Datos.objects.all()
	return render_to_response('index.html',{'usuarios':usuarios},context_instance=RequestContext(request))

def agregar_usuario(request):
	formulario = UsuariosForm()
	return render_to_response("agregar_usuario.html",{'formulario':formulario},context_instance=RequestContext(request))

def agregar_usuario_ajax(request):
	if request.is_ajax() and request.method == 'POST':
		formulario = UsuariosForm(request.POST, request.FILES)
		errores = ''
		exito = False
		if formulario.is_valid():
			formulario.save()
			exito = True
		else:
			errores = formulario.errors
		response = {'exito':exito, 'errores':errores}
		return HttpResponse(json.dumps(response), mimetype="application/json")
	else:
		raise Http404

def eliminar(request,id_usuario):
	usuario = Datos.objects.get(pk=id_usuario)
	usuario.delete()
	return HttpResponseRedirect("/")

def editar(request,id_usuario):
	usuario = Datos.objects.get(pk=id_usuario)
	formulario = UsuariosForm(instance=usuario)
	return render_to_response("editar_usuario.html",{'formulario':formulario},context_instance=RequestContext(request))

def editar_ajax(request):
	if request.is_ajax() and request.method == 'POST':
		usuario = Datos.objects.get(pk=request.POST['id_usuario'])
		formulario = UsuariosForm(request.POST, request.FILES, instance=usuario)
		errores = ''
		exito = False
		if formulario.is_valid():
			formulario.save()
			exito = True
		else:
			errores = formulario.errors
		response = {'exito':exito, 'errores':errores}
		return HttpResponse(json.dumps(response), mimetype="application/json")
	else:
		raise Http404