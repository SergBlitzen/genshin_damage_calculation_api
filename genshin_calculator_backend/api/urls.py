from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('characters', views.CharacterViewSet)
router_v1.register('weapons', views.WeaponViewSet)

urlpatterns = [
    path('v1/calculate/', views.CalculationAPIView.as_view()),
    path('v1/', include(router_v1.urls))
]
