from django.core.context_processors import csrf
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, Http404
from django.views.defaults import page_not_found
from .models import Articulo, ArticuloForm
from pprint import pprint
from django.db.models import Q

from .models import Articulo
from .utils import *

# vista principal
def home(request):
    return render(request, 'inventario/base.html')


# vista del articulo
def ver(request, question_id):
    item = get_object_or_404(Articulo, pk=question_id)
    if request.user.is_authenticated() and item.usuario == request.user:
        return render(request, 'inventario/view_item.html', {'item': item})
    else:
        return page_not_found()


def crear(request):
    form = ArticuloForm()
    if (request.POST and request.user.is_authenticated()):
        f = ArticuloForm(request.POST)
        j = f.save(commit=False)
        j.usuario = request.user
        j.save()
        return HttpResponse('ok')

    data = {'form': form}


def editar(request, id):
    item = get_object_or_404(Articulo, pk=id)

    form = ArticuloForm()
    if request.user.is_authenticated() and item.usuario == request.user:
        if request.POST:
            f = ArticuloForm(request.POST, instance=item)
            f.save()
            data = {}
        else:
            data = {'form': ArticuloForm(instance=item)}
        data.update(csrf(request))
        return render(request, 'inventario/item.html', data)

    else:
        return page_not_found()


def listado(request):
    resp = {}
    query = request.GET.get('query')
    pag = string_to_positive_int_or_default(request.GET.get('pag'), 1)
    cant = string_to_positive_int_or_default(request.GET.get('cant'), 10)
    if query != None:
        count = Articulo.objects.filter(usuario=request.user).filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query)).count()
        resp['cantidad'] = count
        obj = Articulo.objects.filter(usuario=request.user).filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query))[(pag-1)*cant:pag*cant]
    else:
        obj = Articulo.objects.filter(usuario=request.user)[(pag - 1) * cant:pag * cant]
        count = Articulo.objects.filter(usuario=request.user).count()
        resp['cantidad'] = count
    resp['lista'] = obj
    return render(request, 'inventario/list.html', resp)