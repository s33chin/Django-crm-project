from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), # type: ignore
    #path('login/', views.login_user, name='login'), # type: ignore
    path('logout/', views.logout_user, name='logout'), # type: ignore
    path('register/', views.register_user, name='register'),  # type: ignore

]
