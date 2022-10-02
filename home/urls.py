from django.urls import path
from .views import HomeTemplateview, MenuTemplateview

urlpatterns = [
    path('', HomeTemplateview.as_view(), name='home'),
    path('menu/', MenuTemplateview.as_view(), name='menu'),
]
