from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import signup

urlpatterns = [
    path('login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('signup/', signup, name='signup'),
]
