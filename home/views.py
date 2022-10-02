from django.shortcuts import render
from django.views.generic import TemplateView

from category.models import Category
from option.models import Option


class HomeTemplateview(TemplateView):
    template_name = "home/home.html"
    

class MenuTemplateview(TemplateView):
    template_name = "home/menu.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recommended"] = Option.objects.filter(recommended=True)
        context["categories"] = Category.objects.all()
        return context
    

