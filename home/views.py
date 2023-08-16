from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    student_info = [
        {"name":"Abdullah", "age": 20, "roll":455035, "department":"Computer Technology"},
        {"name":"Mamun", "age": 19, "roll":455036, "department":"Civil Technology"},
        {"name":"Abdullah Al Mamun", "age": 21, "roll":455037, "department":"Electrical Technology"},
        {"name":"Md Abdullah Al Mamun", "age": 22, "roll":455038, "department":"Computer Science & Technology"},
    ]
    return render(request, 'home/index.html', context = {"student_info":student_info})
