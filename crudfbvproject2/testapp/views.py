from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import  Student

# Create your views here.

def insertview(request):
    form = StudentForm()
    stud_list = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'testapp/index.html',context={'form':form,'stud_list':stud_list})

def deleteview(request,id):
    stud = Student.objects.get(id=id)
    stud.delete()
    return redirect('/')

def updateview(request,id):
    stud = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=stud)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'testapp/update.html', context={'stud':stud})
