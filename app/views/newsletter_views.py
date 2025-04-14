from django.shortcuts import redirect,render
from ..models import *
from django.core.mail import send_mail
from django.contrib import messages

def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        send_mail(
            subject='New Newsletter Subscriber',
            message=f"Email: {email}",
            from_email='dynamixwave@gmail.com',
            recipient_list=['dynamixwave@gmail.com'],
            fail_silently=False,
        )
        newsletter = NewsletterMode.objects.create(
            email=email
        )
        
        context = {
            'email':email,
            'newsletter':newsletter
        }
        # messages.success(request, "Thanks for subscribing to our newsletter!")
        return redirect('HomeList')
    else:
        return redirect('HomeList')