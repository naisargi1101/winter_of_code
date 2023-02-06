from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<int:userId>', views.PostList.as_view(), name='homeUser'),
    path('profile/<int:userId>',views.profile.as_view(),name="profileView"),
    path('createPost/<int:id>/<int:userId>',views.postSave,name="createBlog"),
    path('<slug:slug>/<int:userId>', views.postDetail, name='post_detail'),
    path('summernote/', include('django_summernote.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)