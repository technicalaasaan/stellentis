from rest_framework import routers
# from django.urls import path, include
from .viewsets import VsEmployee

emp_url = routers.DefaultRouter()
emp_url.register('employee', VsEmployee)
