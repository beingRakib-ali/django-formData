from django.shortcuts import render
from .forms import StudentRegister
# Create your views here.


def  studentinfo(request):
    if request.method=='POST':   
     fm = StudentRegister(request.POST)
     if fm.is_valid():
         name = fm.cleaned_data['name']
         email = fm.cleaned_data['email']
         password = fm.cleaned_data['password']
         print(name)
         print(email)
         print(password)
         fm = StudentRegister()
         
    else:
         fm = StudentRegister()
         print('This is GET Methods')
    return render(request,'student.html',{'form':fm})     