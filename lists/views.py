from models import *
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
import pdb


def home(request):
    return render_to_response("index.html",
        None,
        context_instance=RequestContext(request)
    )


def sandbox(request):
    return render_to_response("sandbox.html",
        None,
        context_instance=RequestContext(request)
    )


def view_user_list(request, list_name):
    if request.user.is_authenticated():
        list = get_or_create_list(request.user, list_name)
        return render_to_response("list.html", locals(), context_instance=RequestContext(request))
    url = reverse('login_user')
    return redirect(url)



def view_user(request, user_name):
    user = get_or_create_user(user_name)
    tags = Tag.objects.filter(owner=user)
    return render_to_response("user.html", locals(), context_instance=RequestContext(request))


def view_list(request, user_name, list_name):
#    import pdb; pdb.set_trace()
    user = get_or_create_user(user_name)
    list = get_or_create_list(user, list_name)
    tags = list.get_tags()
    #if list_name == "inbox":
    #    list_items = Item.objects.all()
    #else:
    todo_items = list.item_set.filter(complete=False).order_by('order')
    complete_items = list.item_set.filter(complete=True).order_by('order')
    user_lists = user.list_set.all().order_by('name')
    return render_to_response("list.html", locals(), context_instance=RequestContext(request))


def add_item(request, user_name, list_name, new_item):
    user = get_or_create_user(user_name)
    list = get_or_create_list(user, list_name)
    list.save()
    item = Item(name=new_item, order=list.item_set.count())
    item.list = list
    item.save()
    result = {"name": item.name, "pk": item.pk, "order": item.order}
    return HttpResponse(simplejson.dumps(result))


@csrf_exempt
def move_item(request, pk, list_name, user_name):
    after = request.POST['order']
    item = Item.objects.get(pk=pk)
    item.move(after)
    result = {"name": item.name, "pk": item.pk, "order": item.order}
    return HttpResponse(simplejson.dumps(result))


@csrf_exempt
def tag_action(request, user_name, action):
    pk = request.POST['pk']
    user = get_or_create_user(user_name)

    item = Item.objects.get(pk=pk)

    tag_name = request.POST['tag'].lower()

    #pdb.set_trace()
    tags = Tag.objects.filter(name=tag_name)
    if len(tags) == 1:
        tag = tags[0]
    else:
        tag = Tag(name=tag_name)
        tag.owner = user
        tag.save()
    if action == "remove":
        item.tags.remove(tag)
        item.save()
    elif action == "add":
        item.tags.add(tag)
        item.save()
    else:
        return HttpResponse(simplejson.dumps({"status": "fail"}))
    return HttpResponse(simplejson.dumps({"status": "ok"}))


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


@csrf_exempt
def update_item(request, user_name, list_name, pk):
    item = Item.objects.get(pk=pk)
    if Item:
        complete = request.POST['complete'] == "true"
        item.complete = complete
        item.save()
        return HttpResponse(simplejson.dumps({"status": "ok"}))
    else:
        return HttpResponse(simplejson.dumps({"status": "fail"}))


def clear_list(request, user_name, list_name):
    user = get_or_create_user(user_name)
    list = get_or_create_list(user, list_name)
    list.item_set.all().delete()
    list.delete()
    return HttpResponse(simplejson.dumps({"status": "ok"}))


def get_or_create_user(user_name):
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
