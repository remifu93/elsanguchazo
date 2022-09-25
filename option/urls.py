from django.urls import path
from .views import OptionListView

urlpatterns = [
    path('', OptionListView.as_view(), name='option-list'),
] 