from django.urls import path
from app.views import HomeView, post_detail
from app.vars import NAME
from app import views

app_name = NAME

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('signup/', views.signup, name='signup'),
    path('blog/', views.blog, name='blog'),
    path('post_detail/<int:pk>/', views.post_detail, name='post-detail'),
 path('post_edit/<int:pk>/', views.post_edit, name='post-edit'),
] 
