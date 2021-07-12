from django.urls import path
from .views import  SnackListView, PathView
urlpatterns = [
    path("", SnackListView.as_view(), name = "home"),
    path("<int:pk>", PathView.as_view(), name = "details"),
]