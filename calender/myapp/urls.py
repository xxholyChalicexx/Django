from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calender', views.calender, name='calender'),
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('view/<int:pk>', views.details, name='details'),
    path('view/delete/<int:pk>', views.delete, name='delete'),
    path('view/add', views.add, name='add'),
    path('register', views.signup, name='signup')
]