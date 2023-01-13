from django.shortcuts import render
from .models import Employee
from django.http.response import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import EmployeeForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    print('req', request.GET)
    return HttpResponse({"name" : "Stellentis"}, content_type="application/json")

@csrf_exempt
def sample(request):
    print(request.GET.get('qualification'))
    # data = Employee.objects.get(qualification='BA')
    data = Employee.objects.all()
    # data = Employee.objects.filter(qualification='BA')
    obj = {
        "first_name": "abhinav",
        # "address": "TN"
    }
    # data = Employee.objects.create(**obj)
    # print(dir(Employee.objects))
    # data = Employee.objects.create(first_name="abhinav", address='')
    # print('address', data.address, bool(data.address))
    # data = Employee.objects.filter(pk=5)
    # print(data)
    # if data:
    #     data.delete()
    # print(data, type(data), dir(data))
    return render(request, 'index.html', {'data': data})


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeView(CreateView): #
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/test.html'
    success_url = '/sample'
    # fields = '__all__'
