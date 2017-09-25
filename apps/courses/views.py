from django.shortcuts import render, HttpResponse, redirect
from models import Course
#from django.contrib import messages

def index(request):
  return render(request, 'index.html', {'courses':Course.objects.all()})

def create(request):
  Course.objects.create(name=request.GET['name'], desc=request.GET['desc'])
  return redirect("/courses")

def delete(request, id):
  return render(request, 'courses_destroy.html', {'course':Course.objects.get(id=id)})

def destroy(request, id):
  Course.objects.get(id=id).delete()
  return redirect("/courses")