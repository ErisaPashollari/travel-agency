from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, "core/index.html")


class HomeView(TemplateView):
    template_name = "core/index.html"
