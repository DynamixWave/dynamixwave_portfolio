from django.shortcuts import redirect,render
from ..models import *

def error(request):
    return render(request , '404.html')