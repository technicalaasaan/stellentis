from rest_framework import viewsets
from .models import Employee
from .serializers import SerEmployee

class VsEmployee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = SerEmployee