from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projects/<int:pk>/', views.details, name='project_detail'),
    path('resume/', views.resume_view, name='resume'),
    
]