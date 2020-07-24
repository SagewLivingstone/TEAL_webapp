from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('land/<int:land_id>', views.land_detail, name='land_detail'),
]
