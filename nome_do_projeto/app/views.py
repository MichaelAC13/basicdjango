from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    queryset = models.Users.objects.get(id=31)
    data = {}
    data["email"] = queryset.email
    return HttpResponse(queryset.email)

def rendertemplate(request):
    queryset = models.Users.objects.get(id=31)
    data = {}
    data["email"] = queryset.email
    return render(request, "app.html")
