from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("samuel", views.samuel, name="samuel"),
    # path("<str:name>", views.greet, name="greet"),
    path("<str:name>", views.greeting, name="greeting")
]