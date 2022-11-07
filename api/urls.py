from django.urls import path

from .views import get_data_list

urlpatterns = [path("data/", get_data_list)]
