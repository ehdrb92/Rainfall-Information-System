from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import RequestDataSerializer, RequestAlarmSerializer
from .utils.services import DataRequestService
from .utils.updater import ScheduleUpdater

data_request_service = DataRequestService()
schedule_updater = ScheduleUpdater()


@api_view(["GET"])
def get_data_list(request):
    params = request.data
    num = request.GET.get("num", 50)
    serializer = RequestDataSerializer(data=params)
    serializer.is_valid()
    response = data_request_service.request_data(
        num=num,
        **serializer.data,
    )
    return JsonResponse({"res": response, "status": status.HTTP_200_OK})


@api_view(["GET"])
def get_drain_pipe_alarm(request):
    params = request.data
    serializer = RequestAlarmSerializer(data=params)
    serializer.is_valid()
    schedule = schedule_updater.start_request_drain_pipe(**serializer.data)
    return JsonResponse({"msg": schedule})


@api_view(["GET"])
def get_rain_fall_alarm(request):
    params = request.data
    serializer = RequestAlarmSerializer(data=params)
    serializer.is_valid()
    schedule = schedule_updater.start_request_rain_fall(**serializer.data)
    return JsonResponse({"msg": schedule})


@api_view(["GET"])
def stop_alarm_service(request):
    params = request.data
    schedule_updater.end_scheduler(params["id"])
    return JsonResponse({"msg": "End scheduler"})
