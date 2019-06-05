from django.urls import path
from .views import index
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', index, name='main_page'),
    path('about/', TemplateView.as_view(template_name='about/about.html'), name='about')
]
