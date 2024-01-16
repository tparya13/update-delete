from django.shortcuts import render
from .models import Task
# Create your views here.
def Home(req):
    tasks=Task.objects.all()
    if req.method=="POST":
        task=req.POST["task"]
        priority=req.POST["priority"]
        img=req.FILES['image']
        Date=req.POST.get('date','')
        todo=Task(task=task,priority=priority,Date=Date,img=img)
        todo.save()
    return render(req,'index.html',{"tasks":tasks})


def Update(req,id):
    tasks=Task.objects.get(id=id) 
    if req.method=="POST":
        task=req.POST.get('task','')
        priority=req.POST.get('priority','')
        Task.objects.filter(id=id).update(task=task,priority=priority)
        return redirect("home")
    return render(req,'formUpdate.html',{"task":tasks,'f':f})       

def Delete(req,id):
    tasks=Task.objects.get(id=id) 
    if req.method=="POST":
        Task.objects.filter(id=id).delete()
        return redirect("home")
    return render(req,'delete.html',{"task":tasks})  

