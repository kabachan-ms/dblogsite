from django.http import HttpResponse
from django.views.generic import TemplateView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView


from django.contrib.auth.models import User



def index(request):
    return render(request, 'Dblog/index.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


