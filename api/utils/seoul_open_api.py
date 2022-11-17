import json
from typing import List

from django.conf import settings
import requests


class SeoulOpenAPI:
    def __init__(self) -> None:
        self.auth_key = settings.AUTHENTICATION_KEY


class DrainPipeAPI(SeoulOpenAPI):
    def __init__(self) -> None:
        super().__init__()

    def request_drain_pipe_monitoring_info(
        self,
        gubn: str,
        mea_ymd: str,
        mea_ymd2: str,
        num: int = 10,
    ) -> List[dict]:
        """
        서울시 하수관로 수위 현황 데이터를 응답합니다.
        """
        request = f"http://openAPI.seoul.go.kr:8088/{self.auth_key}/json/DrainpipeMonitoringInfo/1/{num}/{gubn}/{mea_ymd}/{mea_ymd2}"
        response = requests.get(request)
        result = json.loads((response.content).decode("utf-8"))
        return result["DrainpipeMonitoringInfo"]["row"]


class RainfallAPI(SeoulOpenAPI):
    def __init__(self) -> None:
        super().__init__()

    def request_list_rainfall(
        self,
        num: int = 10,
        gu_name: str = None,
    ) -> List[dict]:
        """
        서울시의 각 강우량계에 측정된 10분 누적 강우량 정보를 응답합니다.
        """
        request = f"http://openAPI.seoul.go.kr:8088/{self.auth_key}/json/ListRainfallService/1/{num}/{gu_name}"
        response = requests.get(request)
        result = json.loads((response.content).decode("utf-8"))
        return result["ListRainfallService"]["row"]
