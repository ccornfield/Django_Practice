from django.shortcuts import render

def get_todo_list(request):
    return render(request, 'todo/todo_list.html')



    
# Create your views here.
