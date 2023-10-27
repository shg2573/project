from django.shortcuts import render,HttpResponseRedirect
from todo.models import todo
# Create your views here.
def home (request):
    
    dets=todo.objects.all()
    context={
        "dets":dets,
    }
    return render(request, 'index.html',context)
def add(request):
    if request.method == 'POST':
        content=request.POST.get('content')
        ob=todo(content=content)
        ob.save()
        print("success")
    return HttpResponseRedirect("/")



def dele(request, todoid):
    print(todoid)
    todo.objects.get(id=todoid).delete()
    return HttpResponseRedirect("/")
