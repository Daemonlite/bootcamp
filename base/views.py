from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from base.models import *
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('course-list')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('course-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('course-list')
        return super(RegisterPage, self).get(*args, **kwargs)

class CourseList(LoginRequiredMixin,ListView):
    model = Student
    context_object_name = 'course'
    template_name='base/course_list.html'

class Student(LoginRequiredMixin,CreateView):
    model= Student
    fields = ['full_name','age','email','course']
    template_name='base/student.html'
    success_url = reverse_lazy('course-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Student, self).form_valid(form)

class Tutor(LoginRequiredMixin,CreateView):
    model= Tutor
    fields = ['full_name','age','cv','email','course']
    template_name='base/tutor.html'
    success_url = reverse_lazy('course-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Tutor, self).form_valid(form)


class Newsletter(LoginRequiredMixin,CreateView):
    model= Newsletter
    fields = ['email']
    template_name='base/newsletter.html'
    success_url = reverse_lazy('course-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Newsletter, self).form_valid(form)