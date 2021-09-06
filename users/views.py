from django.shortcuts import render
from users.models import users_list

# Create your views here.

def buscar_user(request):

    return render(request, "buscar_user.html")

def show_user(request):
    username = request.GET["usr"]
    print(username)
    user = users_list.objects.get(name=username)
    print(user)
    context = {
        "user":  user
    }

    return render(request, "user_show.html", context)
