from models import *
from django.shortcuts import render_to_response


def view_list(request, list_name):
    existing_list = List.objects.filter(name=list_name)
    if len(existing_list) == 1:
        list = existing_list[0]
    else:
        list = List(name=list_name)
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