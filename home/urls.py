from django.urls import path
from home import views

urlpatterns = [
    path('all-students/', views.student_list),
]