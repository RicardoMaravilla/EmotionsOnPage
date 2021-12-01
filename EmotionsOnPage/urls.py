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
    path("register_user/", users_views.register_request_user, name="register"),
    path("register_psicologo/", users_views.register_psicologo, name="register_psicologo"),
    path("home_user/", users_views.home_user, name="home_user"),
    path("home_psicologo/", users_views.home_psicologo, name="home_psicologo"),
    path("login/", users_views.login_request, name="login"),
    path("logout/", users_views.logout_request, name= "logout"),
    path("password/", users_views.change_psswd, name="change_psswd"), #para el cambio de password
    path("journal/", users_views.write_journal, name="journal"), 
    path("terms/", users_views.show_terms, name="terms"), 
    path("privacy/", users_views.show_privacy, name="privacy"), 
    path("test/", users_views.show_test, name="test"), 
    path("emociones/",users_views.show_emociones,name="emociones"),
    path("Login/",users_views.show_Login,name="Login"),
    path("recomendaciones/",users_views.show_recomendaciones,name="recomendaciones"),
    path("wikis/",users_views.show_wikis,name="wikis"),
]
