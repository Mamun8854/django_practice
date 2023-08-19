from django.contrib import admin
from django.urls import path, include
from home.views import *

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("delete-student/<id>/", delete_student, name="delete_student"),
    path("update-student/<id>/", update_student, name="update_student"),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
