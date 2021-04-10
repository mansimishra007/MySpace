from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome, name='welcome'),  #url, welcome class from views, name of the page is welcome
    path('home/', views.home, name='home'),
    path('hostel_info/', views.show_hostel_info, name='hostel_info'),

]