from django.urls import path
from . import views  # , include

urlpatterns = [
    # path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('', views.portal, name='portal'),
]