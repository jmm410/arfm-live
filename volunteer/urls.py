from django.urls import path
from . import views

urlpatterns = [
   
    path("", views.index, name="index"),
    path("make_turtle/", views.registerPage, name="make_turtle"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("create/", views.volunteer_create, name="volunteer_create"),
    path("volunteer/<int:volunteer_id>", views.volunteer_read, name="volunteer"),
    path("volunteer_update/<int:volunteer_id>", views.volunteer_update, name="volunteer_update"),
    path("volunteer_delete/<int:volunteer_id>", views.volunteer_delete, name="volunteer_delete"),
    path("volunteers/", views.volunteer_list, name="volunteer_list"),
]