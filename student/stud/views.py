
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Student

class Add_student(CreateView):
    model = Student
    fields = "__all__"


class List_student(ListView):
    model = Student

class Detail_student(DetailView):
    model = Student


class Update_student(UpdateView):
    model = Student

    fields = "__all__"
    success_url = "/"

class Delete_student(DeleteView):
    model = Student
    success_url = "/"
    template_name = "stud/Student_confirm_delete.html"
