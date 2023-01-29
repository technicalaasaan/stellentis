from django.shortcuts import render, redirect
from .models import Employee
from django.http.response import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import EmployeeForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    print('req', request.GET)
    return HttpResponse({"name" : "Stellentis"}, content_type="application/json")

def login_page(request):
    print("am in login page")
    if request.method == "POST":
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        print('un', uname, pwd)
        user_data = authenticate(request, username=uname, password=pwd)
        print('user', user_data)
        if user_data:
            login(request, user_data)
            return redirect('/sample')
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pwd1 = request.POST.get('password')
        pwd2 = request.POST.get('password2')
        if pwd1 != pwd2:
            return HttpResponse('Invalid Password', status=400)
        if User.objects.filter(username=uname):
            return HttpResponse('Username Exist', status=400)
        user_data = User.objects.create(
            username = uname,
            email = email,
            password = pwd1
        )
        if user_data:
            login(request, user_data)
            return redirect('/sample')
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def report_mailer(request):
    subject = "Report Mailer"
    msg = f"""
        <html><body>
        <h1> Welcome to Credo Quiz </h1>
        <h2> Hi! { request.user }</h2>
        <h3> Your Result! </h3>
        </body></html>
    """
    print('resp', subject, msg, settings.DEFAULT_FROM_EMAIL, [request.user.email,])
    # out = send_mail(subject, msg, settings.DEFAULT_FROM_EMAIL, [request.user.email,])
    out = EmailMessage(subject, msg, settings.DEFAULT_FROM_EMAIL, [request.user.email,])
    out.content_subtype = "html"
    out.send()
    print('email out', out)
    return redirect(resolve_url('report'))

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

def mailer(request):
    # send_mail(
    #     'Test mail', #subject
    #     'Hi Hello', #message
    #     settings.EMAIL_HOST_USER,
    #     # [i.email for i in Employee.objects.all()]
    #     ['technicalaasaan@gmail.com',]
    # )
    msg=f"""
        <html><body>
        <h1 style='color:red;'> Welcome to Credo </h1>
        <h2> Hi!</h2>
        <h3> <a href="credo Thanks for Joining! </h3>
        </body></html>
    """
    out = EmailMessage("Test Mail", msg, settings.EMAIL_HOST_USER, ["technicalaasaan@gmail.com", ])
    out.content_subtype = "html"
    out.send()
    return HttpResponse("Mail sent Successfully!")

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeView(CreateView): #
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/test.html'
    success_url = '/sample'
    # fields = '__all__'

# drf -> django rest framework
# POST
# GET
# PATCH
# PUT
# DELETE
# OPTION


"""
Front end <->  BACKEND <-> DATABASE
HTML/JS/CSS    PYTHON      MYSQL
               FRAMEWORK
               
single URL to run both baclend & frontend   RENDERING
               
               
Rendering <---- API
Django Front API Django Backend 
"""