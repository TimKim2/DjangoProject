# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    msg = "my message"
    return render(request, 'home/index.html', {'message' : msg})
# Create your views here.
