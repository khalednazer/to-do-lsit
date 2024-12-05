from django.urls import path
from . import views
from django.contrib.auth.views import  LogoutView

urlpatterns = [
    path('logout/',LogoutView.as_view(next_page = 'login'), name='logout'),
    path('Login/', views.Loginn.as_view(), name='login'),
    path('createacoount/', views.Regeister.as_view(), name='createaccount'),
    path('', views.miand, name='mainPage'),
    path('lists', views.showList, name='listss'),
    path('Taskview', views.Taskview.as_view(), name='Taskview'),
    path('Task/<int:pk>', views.TaskDetil.as_view(), name='task'),
    path('creat', views.creatTask.as_view(), name='creatTask'),
    path('update/<int:pk>', views.updateTask.as_view(), name='upeated'),
    path('Delte/<int:pk>', views.DelteTask.as_view(), name='Delte'),

]


#https://www.youtube.com/watch?v=llbtoQTt4qw&list=PL-51WBLyFTg38qZ0KHkJj-paDQAAu9HiP&index=16&ab_channel=DennisIvy
# https://chatgpt.com/c/674f5999-2cbc-8003-8912-cc4a6273c83b