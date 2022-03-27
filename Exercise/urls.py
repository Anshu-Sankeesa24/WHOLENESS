from django.urls import path
from Exercise import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home',views.home,name='home'),
    path('signup',views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]