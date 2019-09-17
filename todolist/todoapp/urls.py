from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add-task', views.add_task, name='add-task'),
    path('del-task', views.del_task, name='del-task'),
    path('done-task', views.done_task, name='done-task'),
    path('filed-task', views.filed_task, name='filed-task'),
    path('api', views.TasksApi.as_view(), name='api'),
    path('o', include('oauth2_provider.urls', namespace='o')),
]