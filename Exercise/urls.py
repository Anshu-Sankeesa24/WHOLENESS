from django.urls import path
from Exercise import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup',views.register,name='register'),
    path('login', views.login, name='signin'),
    path('logout', views.logout, name='logout'),
   
    #path('activate/<uidb64>/<token>', views.activate, name='activate'),
]