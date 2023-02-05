from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('<int:userId>', views.PostList.as_view(), name='homeUser'),
    path('profile/<int:userId>',views.profile.as_view(),name="profileView"),
    path('createPost/<slug:slug>/<int:userId>',views.postSave,name="createBlog"),
    path('<slug:slug>/<int:userId>', views.postDetail, name='post_detail'),
    path('summernote/', include('django_summernote.urls')),
]