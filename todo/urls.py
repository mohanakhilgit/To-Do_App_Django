from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('edit/<int:task_id>/', views.update, name='update'),

]
