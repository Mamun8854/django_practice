from django.urls import path
from home import views

urlpatterns = [
    # for function based api
    # path('all-students/', views.student_list),

    # for class based api
    path('students-list/', views.studentAPI.as_view()),
    path('students/', views.allStudentAPI.as_view()),
    path('all/', views.studentList.as_view()),
]
