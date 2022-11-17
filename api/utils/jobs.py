import time

from .seoul_open_api import DrainPipeAPI, RainfallAPI
from .services import EmailService

drain_pipe_api = DrainPipeAPI()
rain_fall_api = RainfallAPI()
email_service = EmailService()


def drain_pipe_schedule_api(
    level: int,
    email: str,
    gubn: str,
) -> dict:
    # 요청 시 날짜 및 시간 데이터 가공을 위한 코드
    curr_mon = time.localtime().tm_mon
    if len(str(time.localtime().tm_mon)) == 1:
        curr_mon = f"0{time.localtime().tm_mon}"
    curr_mday = time.localtime().tm_mday
    if len(str(time.localtime().tm_mday)) == 1:
        curr_mday = f"0{time.localtime().tm_mday}"
    curr_hour = time.localtime().tm_hour
    if len(str(time.localtime().tm_hour)) == 1:
        curr_hour = f"0{time.localtime().tm_hour}"

    mea_ymd = f"{time.localtime().tm_year}{curr_mon}{curr_mday}{curr_hour}"
    mea_ymd2 = f"{time.localtime().tm_year}{curr_mon}{curr_mday}{curr_hour}"

    response = drain_pipe_api.request_drain_pipe_monitoring_info(
        gubn=gubn,
        mea_ymd=mea_ymd,
        mea_ymd2=mea_ymd2,
    )
    for data in response:
        if data["MEA_WAL"] >= level:
            email_service.send_alarm_mail(
                data=data["MEA_WAL"],
                email=email,
            )
    print("Check Drain Pipe LEVEL")
    print(
        f"Time {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}"
    )


def rain_fall_schedule_api(
    level: int,
    email: str,
    gu_name: str,
) -> dict:
    response = rain_fall_api.request_list_rainfall(gu_name=gu_name)
    for data in response:
        if data["RAINFALL10"] >= level:
            email_service.send_alarm_mail(
                data=data["RAINFALL10"],
                email=email,
            )
    print("Check Rain Fall LEVEL")
    print(
        f"Time {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}"
    )
