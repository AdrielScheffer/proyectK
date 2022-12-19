from django.shortcuts import render
from django.http import HttpResponse
from playground import templates
from django.views.generic import ListView, CreateView
from .models import Autists
from .forms import OpinionForm
from .filters import ListingFilter
# Create your views here.


class Home(ListView):
    model= Autists
    template_name = 'hello.html'
    
class Opinion(CreateView):
    model= Autists
    form_class = OpinionForm
    template_name= 'opinion.html'


class ShowOpinions(ListView):
    
    model = Autists
    template_name = 'results.html'

    queryset = Autists.objects.all()
    context_object_name = "autists"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ListingFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context
        


    
