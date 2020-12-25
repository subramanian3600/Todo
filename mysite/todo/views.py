from django.http import response
from .models import Task
from django.shortcuts import  render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,admin_only
from django.contrib.auth.models import Group
from .models import Task
from .forms import TaskForm,CreateUserForm

@login_required(login_url='login')
@admin_only
def dashboard(request):

    context={}

    return render(request,'dashboard.html',context)

@login_required(login_url='login')
def home(request):
    tasks=Task.objects.all()
    
    form=TaskForm()
    
    if (request.method =='POST'):
        form=TaskForm(request.POST)
        
        if form.is_valid():
            form.save()

    context={'tasks':tasks,'form':form}
    
    return render(request,'home.html',context)


@unauthenticated_user
def register(request):
        regform=CreateUserForm()

        if request.method =="POST":
            regform=CreateUserForm(request.POST)
            if regform.is_valid():
                user=regform.save()
                username=regform.cleaned_data.get('username')

                group=Group.objects.get(name='aliens')
                user.groups.add(group)

                messages.success(request, 'Account Created !'+ username)
                return redirect('login')

        context={'regform':regform}

        return render(request,'register.html',context)

        

    
@unauthenticated_user
def loginPage(request):

    if request.method =='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username or password is incorrect')
            

    context={}

    return render(request,'login.html',context)
        

    
@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
    
@login_required(login_url='login')
def updateTask(request,pk):
    edit=Task.objects.get(id=pk)
    form=TaskForm(instance=edit)
    

    if request.method =='POST':
        form=TaskForm(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form }
    return render(request,'update.html',context)


@login_required(login_url='login')
def deleteTask(request,pk):
    item=Task.objects.filter(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('/')

    context={'item':item}

    return render(request,'delete.html',context)
