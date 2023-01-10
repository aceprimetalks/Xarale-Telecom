from django.shortcuts import render
from .models import Staff, Staff_Social
from django.views.generic import ListView



# view for Company Staffs


class StaffList(ListView):
    model = Staff
    context_object_name = 'team'
    template_name='team.html'

class Staff_SocialList(ListView):
    model = Staff_Social
    context_object_name = 'staff_socials'
    template_name='team.html'
