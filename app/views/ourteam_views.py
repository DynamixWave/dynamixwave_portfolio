from django.shortcuts import render,redirect,get_object_or_404
from ..models import *

def Ourteam(request):
    ourteam = OurTeamMemberModel.objects.all()
    
    context = {
        'ourteam':ourteam
    }
    return render (request, 'ourteam.html', context)

def Ourteam_detail(request, pk):
    
    ourteam = get_object_or_404(OurTeamMemberModel, id=pk)
    
    context = {
        'team':ourteam
    } 
    return render (request, 'ourteam_detail.html', context)