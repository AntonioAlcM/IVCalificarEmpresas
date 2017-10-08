#-*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import Context
from Calificar.forms import FormCreacionEmpresa
from Calificar.models import cliente_de_mongo
from django.http import JsonResponse
from django.core import serializers
import json
from bson import json_util

def index(request):
    return render(request, 'index.html')

def redireccionar(request):
    return render(request,'CrearEmpresa.html', {'form': FormCreacionEmpresa()})

def crearEmpresa(request):
    if request.method == 'POST':
        form = FormCreacionEmpresa(request.POST)
        if form.is_valid():
            return anhadirEmpresa(request,form)
        else:
            print("Los errores son: ", form.errors.as_data())
    else:
        form = FormCreacionEmpresa()
        return render(request, 'index.html')
def anhadirEmpresa(request,form):
    db=cliente_de_mongo.empresa
    collection=db.empresas
    if collection.find({"Empresa_id" : form.cleaned_data['Empresa_id']}).count()==0:
        collection.insert({  "Nombre" : form.cleaned_data['Nombre'],"AnhoCreacion" : form.cleaned_data['AnhoCreacion'],"Empresa_id" : form.cleaned_data['Empresa_id'], "Calificacion" : "0"})
        return buscarEmpresa(request,form.cleaned_data['Empresa_id'])
    else:
        return render(request,'index.html')

def buscarEmpresa(request,identificador):
    db=cliente_de_mongo.empresa
    collection=db.empresas
    get =collection.find({"Empresa_id" : identificador})
    context=Context({'record':get[0]})
    return  render(request,'infoEmpresa.html', context)

def verEmpresas(request):
    db=cliente_de_mongo.empresa
    collection=db.empresas
    get =collection.find()[:10]
    context=Context({'coleccion':get})
    return render(request,'verEmpresas.html', context)

def verRanking(request):
    db=cliente_de_mongo.empresa
    collection=db.empresas
    get =collection.find()[:10].sort([ ("Calificacion",-1) ])
    context=Context({'coleccion':get})
    return render(request,'verRanking.html', context)

def seleccionarEmpresa(request,identificador):
    db=cliente_de_mongo.empresa
    collection=db.empresas
    get =collection.find({"restaurant_id" : identificador})
    context=Context({'record':get[0]})
    return  render(request,'calificacionEmpresa.html', context)
