from models import *
from django.shortcuts import render_to_response
from django.contrib.auth.models import User


def view_list(request, list_name):
    existing_list = List.objects.filter(name=list_name)
    if len(existing_list) == 1:
        list = existing_list[0]
    else:
        list = List(name=list_name)
        if not request.user.is_anonymous():
            list.user = request.user
        list.save()

    return render_to_response("list.html", {
            "list": list
        })


def add_item(request, list_name, new_item):
    list = List.objects.get(name=list_name)
    item = Item(name=new_item)
    item.list = list
    item.save()
    return render_to_response("list.html", {
            "list": list
        })


def user_lists(request):
    user = request.user
    #user = get_or_create_user(user_name)
    return render_to_response("user.html", {
            "user": user
        })


def get_or_create_user(user_name):
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        user = User(username=user_name)
        user.save()
    return user
