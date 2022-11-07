import json
from typing import List

from django.conf import settings
import requests


class SeoulOpenAPI:
    def __init__(self) -> None:
        self.auth_key = settings.AUTHENTICATION_KEY

    def request_drain_pipe_monitoring_info(
        self,
        num: int,
        gubn: str,
        mea_ymd: str,
        mea_ymd2: str,
    ) -> List[dict]:
        """
        서울시 하수관로 수위 현황 데이터를 응답합니다.
        """
        self.drain_pipe_monitoring_info_url = f"http://openAPI.seoul.go.kr:8088/{self.auth_key}/json/DrainpipeMonitoringInfo/1/{num}/{gubn}/{mea_ymd}/{mea_ymd2}"
        response = requests.get(self.drain_pipe_monitoring_info_url)
        result = json.loads((response.content).decode("utf-8"))
        return result["DrainpipeMonitoringInfo"]["row"]

    def request_list_rainfall_service(
        self,
        num: int,
        gu_name: str = None,
    ) -> List[dict]:
        """
        서울시의 각 강우량계에 측정된 10분 누적 강우량 정보를 응답합니다.
        """
        self.list_rainfall_service_url = f"http://openAPI.seoul.go.kr:8088/{self.auth_key}/json/ListRainfallService/1/{num}/{gu_name}"
        response = requests.get(self.list_rainfall_service_url)
        result = json.loads((response.content).decode("utf-8"))
        return result["ListRainfallService"]["row"]

    def request_data(
        self,
        num: int,
        gubn: str,
        mea_ymd: str,
        mea_ymd2: str,
    ) -> List[dict]:
        """
        서울시 하수관로 수위 현황과 10분 누적 강우량 정보를 종합하여 응답합니다.
        """
        res_drain_pipe = self.request_drain_pipe_monitoring_info(
            num=num,
            gubn=gubn,
            mea_ymd=mea_ymd,
            mea_ymd2=mea_ymd2,
        )
        gu_name = res_drain_pipe[0]["GUBN_NAM"]
        res_rainfall = self.request_list_rainfall_service(
            num=num,
            gu_name=gu_name,
        )

        return res_drain_pipe + res_rainfall
