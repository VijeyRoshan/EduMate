# URL routing for student_dashboard

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('summarize/', views.summarize, name='summarize'),
    path('quiz/', views.quiz, name='quiz'),
    path('doubt/', views.doubt, name='doubt'),
]
