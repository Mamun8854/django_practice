from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

def home(request):
    student_info = [
        {"name":"Abdullah", "age": 20, "roll":455035, "department":"Computer Technology","group":"B","seisson":"18-19"},
        {"name":"Mamun", "age": 19, "roll":455036, "department":"Civil Technology","group":"A","seisson":"20-21"},
        {"name":"Abdullah Al Mamun", "age": 21, "roll":455037, "department":"Electrical Technology","group":"C","seisson":"19-20"},
        {"name":"Md Abdullah Al Mamun", "age": 22, "roll":455038, "department":"Computer Science & Technology","group":"A","seisson":"19-20"},
    ]
    return render(request, 'home/index.html', context = {"student_info":student_info})


def about(request):
    if request.method == "POST":
        data = request.POST
        student_name = data.get('name')
        student_email = data.get('email')
        student_address = data.get('address')
        student_mobile = data.get('mobile')

        # print(student_name,student_email,student_address,student_mobile)

        Student.objects.create(
            name = student_name,
            email=student_email,
            address = student_address,
            mobile=student_mobile,
        )
        messages.success(request, "Student added successfuly!")
        return redirect("/about")

    all_students= Student.objects.all()
    # print(all_students)
    return render(request, 'home/about.html', context={'students':all_students})

def delete_student(request,id):
    queryset = Student.objects.get(id = id)
    queryset.delete()
    return redirect('/about')