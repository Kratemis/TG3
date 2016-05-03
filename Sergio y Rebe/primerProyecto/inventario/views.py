from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from inventario.forms import CafeForm
from inventario.models import Cafe
 
 
def inventario(request):
	#si es una peticion post
    if request.method == "POST":
    	#asignamos a form el formulario para validar
        form = CafeForm(request.POST)
        #si el formulario es validado correctamente
        if form.is_valid():
        	#creamos una nueva instancia de Post con los campos del form
        	#asi capturamos los valores post
        	newPost = Cafe(Nombre = request.POST["Nombre"], Stock = request.POST["Stock"], Descripcion = request.POST["Descripcion"])
        	#guardamos el post
        	newPost.save()
        	#redirigimos a la ruta con name add_post, que es esta
        	return redirect('inventario')
    else:
    	#si no es una peticion post, asignamos a form 
    	#el form que hemos creado sin datos
        form = CafeForm()
    #siempre devolvemos la misma respuesta
    return render_to_response("inventario.html",{"form":form}, context_instance = RequestContext(request))



def listado():
	listado_cafe = Cafe.objects.all()
	return render(request, 'listado.html', context)
