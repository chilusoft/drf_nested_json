from django.urls import path, include

from . import views
# import and make routes from rest_framework



urlpatterns = [

    path('studentData/', views.student_data_list),
    path('studentData/<int:pk>/', views.student_data_detail),
    path('studentResult/', views.student_result_list),
    path('studentResult/<int:pk>/', views.student_result_detail),
    

]