from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Task
from .serializers import TaskSerializer
from datetime import datetime


# API created and serializated
class TasksApi(generics.ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


# Request for Index
@csrf_exempt
def index(request):

    if not request:
        return HttpResponse(status=404)
    
    return render(
        request, 'todolist.html')


# POST for add a task on the application
@csrf_exempt
def add_task(request):
    title = request.POST.get('title')
    desc = request.POST.get('desc')
    deadline = request.POST.get('deadline')

    Task.objects.create(
        title=title,
        desc=desc,
        deadline=deadline
    )

    if not request:
        return HttpResponse(status=404)
    
    return redirect('index')


@csrf_exempt
def del_task(request):
    task = request.POST.get('id')
    Task.objects.filter(pk=task).delete()
    
    if not request:
        return HttpResponse(status=404)
    
    return HttpResponse(status=200)


@csrf_exempt
def done_task(request):
    task = request.POST.get('id')
    date = datetime.now()
    Task.objects.filter(pk=task).update(complete=True, completed_at=date)
    
    if not request:
        return HttpResponse(status=404)

    return HttpResponse(status=201)


@csrf_exempt
def filed_task(request):
    task = request.POST.get('id')
    Task.objects.filter(pk=task).update(filed=True)
    
    if not request:
        return HttpResponse(status=404)

    return HttpResponse(status=201)