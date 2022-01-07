from django.urls import path, include
from rest_framework import routers

from .views import EmployeeViewSet, home, create_employee, update_employee

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', home, name='home'),
    path('add/', create_employee, name='create'),
    path('<int:pk>/', update_employee, name='update')
]
