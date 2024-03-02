from django.urls import path, include
from rest_framework import routers
from apiRest import views

router = routers.DefaultRouter()
router.register(r'alumno',views.AlumnoViewSet)

urlpatterns=[
    path('',include(router.urls))
]