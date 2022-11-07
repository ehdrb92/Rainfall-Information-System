from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import RequestDataSerializer
from .services import SeoulOpenAPI

seoul_open_api = SeoulOpenAPI()


@api_view(["GET"])
def get_data_list(request):
    params = request.data
    num = request.GET.get("num", 50)
    serializer = RequestDataSerializer(data=params)
    serializer.is_valid()
    response = seoul_open_api.request_data(
        num=num,
        **serializer.data,
    )
    return JsonResponse({"res": response, "status": status.HTTP_200_OK})
