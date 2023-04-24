from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
]


urlpatterns += staticfiles_urlpatterns()