from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset.html"),name='password_reset'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset/password_reset_done.html"),name="password_reset_complete")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)