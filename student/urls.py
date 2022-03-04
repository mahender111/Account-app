
from django.urls import path

from student import views

urlpatterns = [
    path('', views.home, name="home"),
    path('base/',views.base,name="base"),
    path('index/',views.index,name ="index"),
    path('list/',views.data_list,name ="list"),
    path('user/',views.switch,name="switch"),
    path('sal/',views.data_sal,name="salary"),
    path('s/',views.data_salary),
    path('de/',views.delete,name="delete"),

]