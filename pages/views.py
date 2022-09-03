from django.shortcuts import render
from django.views.generic import TemplateView

def homePageView(request):
    return render(request, 'pages/home.html')
