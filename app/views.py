from typing import Any
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import TemplateView,FormView
from app.forms import *

# Context by TemplateView

class Templatehtml(TemplateView):
    template_name='templatehtml.html'
    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Priya'
        ECDO['from']='Odisha'
        return ECDO
    
# Form by using Template View
    
class InsertschoolbyTV(TemplateView):
    template_name='insertschoolTV.html'
    def get_context_data(self,**kwargs):
        ESDO=super().get_context_data(**kwargs)
        ESDO['SFO']=SchoolForm
        return ESDO
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertschoolbyTV is Done')
        
# Form by using Form View Class
           
class InsertschoolbyFV(FormView):
    template_name='insertschoolbyFV.html'
    form_class=SchoolForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('InsertschoolbyFV is Done')