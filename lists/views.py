from models import *
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson


def home(request):
    return render_to_response("index.html",
        None,
        context_instance=RequestContext(request)
    )


def view_list(request, user_name, list_name):
#    import pdb; pdb.set_trace()
    user = get_or_create_user(user_name)
    list = get_or_create_list(user, list_name)

    user_lists = user.list_set.all()
    return render_to_response("list.html", {
            "list": list,
            "list_items": list.item_set.all(),
            "user_lists": user_lists
        }, context_instance=RequestContext(request))


def add_item(request, user_name, list_name, new_item):
    user = get_or_create_user(user_name)
    list = get_or_create_list(user, list_name)
    list.save()
    item = Item(name=new_item, order=list.item_set.count())
    item.list = list
    item.save()
    result = {"name": item.name, "pk": item.pk}
    return HttpResponse(simplejson.dumps(result))


def remove_item(request, user_name, list_name, pk):
    item = Item.objects.get(pk=pk)
    if item:
        list = item.list
        item.delete()
        if list.item_set.count() == 0:
            list.delete()
        return HttpResponse(simplejson.dumps({"status": "ok"}))
    else:
        return HttpResponse(simplejson.dumps({"status": "fail"}))


def clear_list(request, user_name, list_name):
    user = get_or_create_user(user_name)
    list = get_or_create_list(user, list_name)
    list.item_set.all().delete()
    list.delete()


def get_or_create_user(user_name):
    #user = request.user
    #if not user.is_authenticated():
    #    user = User.objects.filter(username=user_name)
    #    if len(user) == 1:
    #        user = user[0]
    #    else:
    #        user = None
    user = User.objects.filter(username=user_name)
    if len(user) == 0:
        user = User.objects.create_user(user_name, 'test@test.com', 'xyzzy')
        user.save()
    else:
        user = user[0]
    return user


def get_or_create_list(user, list_name):
    existing_list = user.list_set.filter(name=list_name)
    if len(existing_list) == 1:
        list = existing_list[0]
    else:
        list = List(name=list_name)
        list.user = user
    return list
