from django.shortcuts import render, redirect
from  django.http import JsonResponse
from .forms import Instituciones_Form, Inscritos_Form
from .serializers import Instituciones_Serializer, Inscritos_Serializer
from .models import Instituciones, Inscritos
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def usuario(request):
    usu = {
        'nombre': 'Rodolfo',
        'apellido': 'Rivas',
        'RUT': '21383955-1',
        'edad': 20
    }
    return JsonResponse(usu)

def instituciones_form(request):
    if request.method == 'POST':
        form = Instituciones_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Instituciones_Form()
        
    data = {
        'form': form,
        'titulo': 'Formulario de Instituciones'
    }
    return render(request, 'form.html', data)

@api_view(['GET', 'POST'])
def instituciones_list(request):
    if request.method == 'GET':
        instituciones = Instituciones.objects.all()
        serializer = Instituciones_Serializer(instituciones, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = Instituciones_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def instituciones_detalle(request, id):
    try:
        instituciones = Instituciones.objects.get(id=id)
    except Instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Instituciones_Serializer(instituciones)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = Instituciones_Serializer(instituciones, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        instituciones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def inscritos_form(request):
    if request.method == 'POST':
        form = Inscritos_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Inscritos_Form()
        
    data = {
        'form': form,
        'titulo': 'Formulario de Inscritos'
    }
    return render(request, 'form.html', data)

class Inscritos_List(APIView):
    def get(self, request):
        inscritos = Inscritos.objects.all()
        serializer = Inscritos_Serializer(inscritos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Inscritos_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Inscritos_Detalle(APIView):
    def get_object(self, id):
        try:
            return Inscritos.objects.get(id=id)
        except Inscritos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        inscritos = self.get_object(id)
        serializer = Inscritos_Serializer(inscritos)
        return Response(serializer.data)
    
    def put(self, request, id):
        inscritos = self.get_object(id)
        serializer = Inscritos_Serializer(inscritos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        inscritos = self.get_object(id)
        inscritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)