from django.shortcuts import redirect,render
from ..models import *
from django.core.mail import send_mail

def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        user_message = request.POST['message']
        
        send_mail(
            subject=f"{subject}",
            message=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject}\n\nMessage:\n{user_message}",
            from_email=email,
            recipient_list=['dynamixwave@gmail.com'],
            fail_silently=False,
        )
        
        contact = ContactModel.objects.create(
            name=name,
            email=email,
            mobile=phone,
            subject=subject,
            message=user_message,
        )
        
        
        context = {
            'contact':contact,
            'name':name,
        }
        return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html')
    
    
    