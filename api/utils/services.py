from typing import List

from django.core.mail import send_mail
from django.conf import settings

from .seoul_open_api import DrainPipeAPI, RainfallAPI

drain_pipe_api = DrainPipeAPI()
rainfall_api = RainfallAPI()


class DataRequestService:
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
        res_drain_pipe = drain_pipe_api.request_drain_pipe_monitoring_info(
            num=num,
            gubn=gubn,
            mea_ymd=mea_ymd,
            mea_ymd2=mea_ymd2,
        )
        gu_name = res_drain_pipe[0]["GUBN_NAM"]
        res_rainfall = rainfall_api.request_list_rainfall_service(
            num=num,
            gu_name=gu_name,
        )

        return res_drain_pipe + res_rainfall


class AlarmService:
    def __init__(self) -> None:
        pass


class EmailService(AlarmService):
    def send_alarm_mail(self, data: int, email: str):
        subject = "기준 값을 초과하였습니다."
        message = f"측정치 : {data}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(
            subject,
            message,
            email_from,
            recipient_list,
        )
        return "Send an email"
