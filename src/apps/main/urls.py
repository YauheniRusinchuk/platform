from django.urls import path, include
from .views import index
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('home/', include('src.apps.home.urls', namespace='home')),
    path('', index, name='main_page'),
    path('about/', TemplateView.as_view(template_name='about/about.html'), name='about')
]
