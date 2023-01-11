from django.shortcuts import render
from .models import Employee
from django.http.response import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    print('req', request.GET)
    return HttpResponse({"name" : "Stellentis"}, content_type="application/json")

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
