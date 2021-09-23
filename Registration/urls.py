from django.urls import path
from django.views.generic import RedirectView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RedirectView.as_view(url='/home')),
    path('home/', views.index, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('change-password/', views.change_password, name='change-password'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='edit_profile'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete'),
    path('qwerty/<str:pk>', views.getData, name='qwerty'),
    path('sendSMS/<str:pk>', views.startSendSMS, name='sendSMS'),
    path('qrcode_scanner/', views.startQRscanner, name='qrcode_scanner'),
    path('admin/', views.adminLogin, name='admin'),
    path('admin/reports/', views.adminReports, name='reports'),
    path('admin/logout/', views.adminlogoutPage, name='admin-logout'),
    path('admin/logbook/<str:pk>', views.adminLogbook, name='admin-logbook'),
]
