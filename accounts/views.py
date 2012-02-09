from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from accounts.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext


@csrf_exempt
def register(request):
    errors = []
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    return render_to_response("register.html", {
        "form": form},context_instance=RequestContext(request)
    ) 