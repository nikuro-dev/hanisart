from django.urls import path
from . import views

urlpatterns = [
    #main app views
    path('', views.index, name='home')
]
