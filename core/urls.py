from django.urls import path

from core import views


urlpatterns = [
    path("", views.home, name="home"),
    # path("", views.HomeView.as_view(), name="home"),
]
