from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from home.models import Student
from home.serializers import StudentSerializer


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

    all_students= Student.objects.all().order_by('-pk')
    # print(all_students)
    # search by name code start
    
    if request.GET.get('search'): 
        all_students = all_students.filter(name__icontains = request.GET.get('search'))

    # search by name code end

    return render(request, 'home/about.html', context={'students':all_students})

def delete_student(request,id):
    queryset = Student.objects.get(id = id)
    queryset.delete()
    return redirect('/about')

def update_student(request,id):
    queryset = Student.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        student_name = data.get('name')
        student_email = data.get('email')
        student_address = data.get('address')
        student_mobile = data.get('mobile')

        queryset.name = student_name
        queryset.email = student_email
        queryset.address = student_address
        queryset.mobile = student_mobile

        queryset.save()
        return redirect('/about')


    context = {'student':queryset}
    return render(request, 'home/update_student.html',context)


#   For API create 

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)