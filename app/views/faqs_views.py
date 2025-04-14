from django.shortcuts import redirect,render
from ..models import *

def faqs(request):
    return render(request , 'faqs.html')