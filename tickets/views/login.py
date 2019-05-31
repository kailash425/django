from __future__ import unicode_literals
from django.shortcuts import redirect, render
from django.http import HttpResponse

def login(request, **kwargs):
    print(kwargs)
    response = render(request,'login.html')
    return response
