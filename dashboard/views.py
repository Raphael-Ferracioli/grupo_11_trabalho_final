from django.shortcuts import render
from .services import DashboardService


def home(request):
    contexto = DashboardService().montar_contexto(request.user)
    return render(request, 'dashboard/home.html', contexto)
