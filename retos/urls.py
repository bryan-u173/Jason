from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EstadoViewSet, UbicacionViewSet, InventarioViewSet,
    bienvenida_view, login_view, logout_view, dashboard_fbv, DashboardCBV
)

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'ubicaciones', UbicacionViewSet)
router.register(r'inventarios', InventarioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    
    # Vistas Web Autenticación
    path('', bienvenida_view, name='bienvenida'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard-fbv/', dashboard_fbv, name='dashboard_fbv'),
    path('dashboard-cbv/', DashboardCBV.as_view(), name='dashboard_cbv'),
]