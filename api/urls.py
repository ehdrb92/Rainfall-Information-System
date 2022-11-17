from django.urls import path

from .views import get_data_list, get_drain_pipe_alarm, get_rain_fall_alarm, stop_alarm_service

urlpatterns = [
    path("data/", get_data_list),
    path("alarm/drainpipe/", get_drain_pipe_alarm),
    path("alarm/rainfall/", get_rain_fall_alarm),
    path("alarm/stop/", stop_alarm_service),
]
