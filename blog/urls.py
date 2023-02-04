from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='homeUser'),
    path('createPost/',views.postSave,name="createBlog"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('summernote/', include('django_summernote.urls')),
]