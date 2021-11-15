from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic import( CreateView, TemplateView)
from django.views.generic.edit import CreateView
from . import models
# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class Section1_1View( CreateView ):
    template_name = 'section1_1.html'
    model = models.Section1_1
    context_object_name = 'section'
    fields = (   'check1', 
               'check2', 'aItemID2', 'aQty2')
    success_url = reverse_lazy('App:section1_2')
            
    def get_context_data(self, **kwargs):
        context= CreateView.get_context_data(self, **kwargs)
        # form2 = self.form_class2(self.request.GET or None)
        context.update({'section': models.Section1_1 })
        return context

    # def get_success_url(self):
        # return reverse('App:section1_2')


class Section1_2View( CreateView ):
    template_name = 'section1_2.html'
    model = models.Section1_2
    context_object_name = 'section'
    fields = (
        'check1', 'aItemID1',
        'check2', 'aItemID2', 'aQty2'
    )

    def get_context_data(self, **kwargs):
        context= CreateView.get_context_data(self, **kwargs)
        # form2 = self.form_class2(self.request.GET or None)
        context.update({'section': models.Section1_2 })
        return context

    def get_success_url(self):
        return reverse('App:section1_3')
        pass

    
class Section1_3View( CreateView ):
    template_name = 'section1_3.html'
    model = models.Section1_1
    context_object_name = 'section'
    fields = (
        'check1', 'aItemID1',
        'check2', 
    )

    def get_context_data(self, **kwargs):
        context= CreateView.get_context_data(self, **kwargs)
        # form2 = self.form_class2(self.request.GET or None)
        context.update({'section': models.Section1_3 })
        return context

    def get_success_url(self):
        return reverse('App:home')

class Help1_1View( TemplateView ):
    template_name = 'help1_1.html'

class Help1_2View( TemplateView ):
    template_name = 'help1_2.html'

class Help1_3View( TemplateView ):
    template_name = 'help1_3.html'