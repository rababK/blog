from django.urls import path
from . import views
app_name='blog'

urlpatterns=[
    path('',views.home,name="home"),
    path('PostDetails/<int:pk>/',views.PostDetails,name="PostDetails"),
    path('CreatePost/',views.CreatePost,name="CreatePost"),

]