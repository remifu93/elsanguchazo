from django.urls import path
from .views import HomeTemplateview

urlpatterns = [
    path('', HomeTemplateview.as_view(), name='home'),
]
