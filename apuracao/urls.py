from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListResults.as_view(), name='resultados'),
]