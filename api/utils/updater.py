from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import drain_pipe_schedule_api, rain_fall_schedule_api

scheduler = BackgroundScheduler()


class ScheduleUpdater:
    def start_request_drain_pipe(
        self,
        level: int,
        email: str,
        gubn: str,
        minutes: int = 1,
    ) -> str:
        scheduler.add_job(
            drain_pipe_schedule_api,
            "interval",
            kwargs={
                "level": level,
                "email": email,
                "gubn": gubn,
            },
            minutes=minutes,
            id="drain_pipe",
        )
        scheduler.start()

        return "start drain pipe schedule"

    def start_request_rain_fall(
        self,
        level: int,
        email: str,
        minutes: int = 10,
        gu_name: str = None,
    ) -> str:
        scheduler.add_job(
            rain_fall_schedule_api,
            "interval",
            kwargs={
                "level": level,
                "email": email,
                "gu_name": gu_name,
            },
            minutes=minutes,
            id="rain_fall",
        )
        scheduler.start()

        return "start drain pipe schedule"

    def end_scheduler(
        self,
        id: str,
    ) -> str:
        scheduler.remove_job(id)

        return f"stop {id} schedule"
