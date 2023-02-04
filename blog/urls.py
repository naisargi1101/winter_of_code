from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='homeUser'),
    path('createPost/<slug:slug>',views.postSave,name="createBlog"),
    path('profile/',views.profile.as_view(),name="profile"),
    path('<slug:slug>/', views.postDetail, name='post_detail'),
    path('summernote/', include('django_summernote.urls')),
]