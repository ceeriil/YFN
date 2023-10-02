from django.urls import path
from app.views import HomeView
from app.vars import NAME

app_name = NAME

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
