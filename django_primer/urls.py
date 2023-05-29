"""django_primer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import IndexView, EditSubject, EditEvaluations, EditStudent, DeleteEvaluations, RedactEvaluations, \
    DeleteSubject, DeleteStudent, RedactStudent

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('edit_students', EditStudent.as_view(), name='edit_students'),
    path('delete_students', DeleteStudent.as_view(), name='delete_students'),
    path('redact_students', RedactStudent.as_view(), name='redact_students'),
    path('edit_subjects', EditSubject.as_view(), name='edit_subjects'),
    path('delete_subjects', DeleteSubject.as_view(), name='delete_subjects'),
    path('edit_evaluations', EditEvaluations.as_view(), name='edit_evaluations'),
    path('delete_evaluations', DeleteEvaluations.as_view(), name='delete_evaluations'),
    path('redact_evaluations', RedactEvaluations.as_view(), name='redact_evaluations'),
]
