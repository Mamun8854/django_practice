from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    student_info = [
        {"name":"Abdullah", "age": 20, "roll":455035, "department":"Computer Technology","group":"B","seisson":"18-19"},
        {"name":"Mamun", "age": 19, "roll":455036, "department":"Civil Technology","group":"A","seisson":"20-21"},
        {"name":"Abdullah Al Mamun", "age": 21, "roll":455037, "department":"Electrical Technology","group":"C","seisson":"19-20"},
        {"name":"Md Abdullah Al Mamun", "age": 22, "roll":455038, "department":"Computer Science & Technology","group":"A","seisson":"19-20"},
    ]
    return render(request, 'home/index.html', context = {"student_info":student_info})


def about(request):
    return render(request, 'home/about.html')