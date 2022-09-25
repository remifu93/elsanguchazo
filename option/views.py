from django.shortcuts import render
from django.views.generic import ListView
from .models import Option
from category.models import Category

class OptionListView(ListView):
    model = Option
    template_name = "option/list.html"
    
    def get_context_data(self, **kwargs):
        category = self.request.GET.get('category', False)
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(name=category)
        return context
    
    
    def get_queryset(self):
        qs = Option.objects.all()
        category = self.request.GET.get('category', False)
        
        if category:
            qs = Option.objects.filter(category__name=category)
        
        return qs
    
    
    
    
