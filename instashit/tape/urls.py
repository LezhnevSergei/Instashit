from django.urls import path
from . import views



urlpatterns = [
    path('', views.TapeView.as_view())
]