from .models import Task
from django.shortcuts import  render,redirect

from .models import Task
from .forms import TaskForm
# Create your views here.
def home(request):
    tasks=Task.objects.all()

    form=TaskForm()
    
    if (request.method =='POST'):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()

    context={'tasks':tasks,'form':form}
    
    return render(request,'home.html',context)

def deleteTask(request,pk):
    item=Task.objects.filter(id=pk)

    if request.method =='POST':
        item.delete()
        return redirect('/')

    context={'item':item}

    return render(request,'delete.html',context)
