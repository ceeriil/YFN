from django.urls import path
from app.views import HomeView
from app.vars import NAME
from app import views

app_name = NAME

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
     path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('blog/', views.blog, name='blog'),
]
