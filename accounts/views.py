from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response, redirect
from django.core import urlresolvers
from django.template import RequestContext
from django.contrib.auth.models import User


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                url = urlresolvers.reverse('client_list')
                return redirect(url)
    return render_to_response("login.html", locals(), context_instance=RequestContext(request))

def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST('email')
        user = User.objects.create_user(username, email, password)
        url = urlresolvers.reverse('view_user', user_name=username)
        return redirect(url)
