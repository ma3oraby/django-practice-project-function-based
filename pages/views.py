from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def index (request) :
    #x={'name':'mohamed ','age':39}
    return render(request,'pages/index.html',{'name':'3or'})

def about (request) : 
    if request.method == 'POST' :
        data_form = LoginForm (request.POST)
        if data_form.is_valid() :
            data_form.save()

    # user_name = request.POST.get('username')
    # password = request.POST.get('password')
    # data = Login(username=user_name,password=password).save()
    return render (request,'pages/about.html',{'lf':LoginForm})