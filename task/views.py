from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def Home(request):
    pro = Projects.objects.all()
    proimg =Profile.objects.all()
    context ={"pro":pro,'proimg':proimg}
    return render(request,'task/dashboard.html',context)

def Project(request):
    temp = Projects.objects.all()
    
    context = {'temp':temp}
    return render(request,'task/myproject.html',context)

def Toview(request,pk):
    toview= Projects.objects.get(id=pk)
    context = {'toview':toview}
    return render(request,'task/view_pro.html',context)    

