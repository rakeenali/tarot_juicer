from django.urls import path, include
from . import views


urlpatterns = [
    path('first_work_order', views.first_work_order, name='first_work_order'),
    path('second_work_order', views.second_work_order, name='second_work_order')
]
