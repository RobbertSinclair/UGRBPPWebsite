from django.urls import path
from bpp_app import views

app_name = "bpp_app"

urlpatterns = [
    path("", views.landing_page, name="landing")
]