from django.urls import path
from base.views import *
from django.contrib.auth.views import LogoutView
urlpatterns=[
     path('login/', CustomLoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
     path('register/', RegisterPage.as_view(), name='register'),

     path('',CourseList.as_view(),name='course-list'),  
     path('student/',Student.as_view(),name='student'),
     path('tutor/',Tutor.as_view(),name='tutor'),
     path('newsletter/',Newsletter.as_view(),name='newsletter'),
]