from django.urls import path
from .views import SignupPageView, HomePageView, AboutPageView

urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("about/", AboutPageView.as_view(), name="about"), 
    path("home/", HomePageView.as_view(), name="home"),
]