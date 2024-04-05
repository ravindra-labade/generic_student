from django.urls import path
from .views import Add_student, List_student, Detail_student, Update_student, Delete_student

urlpatterns = [
    path('add/', Add_student.as_view()),
    path('list/', List_student.as_view()),
    path('detail/<int:pk>/', Detail_student.as_view()),
    path('update/<int:pk>/', Update_student.as_view()),
    path('delete/<int:pk>/', Delete_student.as_view()),
]
