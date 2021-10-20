"""EmotionsOnPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from EmotionsOnPage import views
from users import views as users_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),  # Acá
    path('admin/', admin.site.urls),
    path("register/", users_views.register_request, name="register"),
    path("register_user/", users_views.register_user, name="register_user"),
    path("register_psicologo/", users_views.register_psicologo, name="register_psicologo"),
    path("login/", users_views.login_request, name="login"),
    path("logout/", users_views.logout_request, name= "logout"),
    path("password/", users_views.change_psswd, name="change_psswd"), #para el cambio de password
]
