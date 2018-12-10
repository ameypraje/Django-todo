from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect

# Create your views here..
def index(request):
    all_todo_items=TodoItem.objects.all()
    return render(request,'todo.html',
                  {'all_items':all_todo_items})

def addTodo(request):
    new_items=TodoItem(content=request.POST['content'])
    new_items.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request,todo_id):
    item_to_delete= TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')

