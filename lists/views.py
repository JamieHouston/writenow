from models import *
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext


def view_list(request, list_name):
#    import pdb; pdb.set_trace()
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
        }, context_instance=RequestContext(request))


def add_item(request, list_name, new_item):
    list = List.objects.get(name=list_name)
    item = Item(name=new_item)
    item.list = list
    item.save()


def remove_item(request, list_name, pk):
    item = Item.objects.get(pk=pk)
    item.delete()


def user_lists(request):
    user = request.user
    #user = get_or_create_user(user_name)
    return render_to_response("user.html", {
            "user": user
        }, context_instance=RequestContext(request))


def home(request):
    return render_to_response("index.html",
        None,
        context_instance=RequestContext(request)
    )
