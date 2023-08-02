from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('main/', views.main, name='main'),
    path('item/<int:id>', views.item, name='item'),
    path('formtasks/', views.formtasks, name='formtasks'),
    path("taskdelete/<int:id>", views.taskdelete, name="taskdelete"),
]
