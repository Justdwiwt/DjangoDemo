import os
from django.urls import reverse
from app.forms import MomentForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse("app.views.welcome"))
    else:
        form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'app/templates', 'moments_input.html'), {'form': form})


def welcome(request):
    return HttpResponse('<h1>SUCCESS</h1>')
