"""stellentis URL Configuration

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
from django.urls import path, include
from django.http.response import HttpResponse
from employee.views import sample, EmployeeView
from employee.urls import emp_url
# def home(request):
#     return HttpResponse("Welcome to Credo")

urlpatterns = [
    path('sample/', sample, name='table'),
    path('admin/', admin.site.urls),
    path('employee/', EmployeeView.as_view())
]

urlpatterns += [
    path('api/', include(emp_url.urls))
]