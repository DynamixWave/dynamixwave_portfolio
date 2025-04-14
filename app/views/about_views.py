from django.shortcuts import redirect,render,get_object_or_404
from ..models import *

def AboutList(request):
    abouts = AboutModel.objects.all()
    ourpartners = OurPartnerModel.objects.all()
    counters = CounterModel.objects.all().order_by('-id')[:3]
    ourteam = OurTeamMemberModel.objects.all()
    customerfeedback = CustomerFeedbackModel.objects.all()
    context = {
        'abouts':abouts,
        "ourpartner":ourpartners,
        "counter":counters,
        "ourteam":ourteam,
        "customerfeedback":customerfeedback,
    }
    return render(request, 'about.html', context)