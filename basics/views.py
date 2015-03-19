from django.shortcuts import render
from django.http import HttpResponse
from basics.models import User
import json
from django.core import serializers
from django.template import Context, loader

def index(request):
    t = loader.get_template('basics/index.html')
    c = Context({ })
    return HttpResponse(t.render(c))

def entries(request):
    entries = User.objects.all()
    data = serializers.serialize("json", entries)
    
    return HttpResponse(data, content_type='application/json')
