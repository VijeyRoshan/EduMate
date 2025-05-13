# Django project URLs
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('student_dashboard.urls')),
    path('admin/', admin.site.urls),
]
