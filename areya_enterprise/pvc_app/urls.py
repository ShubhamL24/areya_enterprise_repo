from django.urls import path, include
from pvc_app import views

# Create your urls here.

urlpatterns = [
    path('', views.index_view, name="index_view"),
]
