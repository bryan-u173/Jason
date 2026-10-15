from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Estado, Ubicacion, Inventario
from .serializers import EstadoSerializer, UbicacionSerializer, InventarioSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

def bienvenida_view(request):
    return render(request, 'retos/bienvenida.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard_fbv')
    else:
        form = AuthenticationForm()
    return render(request, 'retos/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('bienvenida')

@login_required(login_url='login')
def dashboard_fbv(request):
    return render(request, 'retos/dashboard_fbv.html')


class DashboardCBV(LoginRequiredMixin, TemplateView):
    template_name = 'retos/dashboard_cbv.html'
    login_url = 'login'