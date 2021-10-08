import datetime


def get_duration(visit):
    visit_enter_time, visit_leave_time = visit.get_visit_localtime()
    delta_time = visit_leave_time - visit_enter_time
    delta_time_seconds = delta_time.total_seconds()
    return delta_time_seconds


def format_duration(duration):
    hours, minutes, seconds = str(datetime.timedelta(seconds=int(duration))).split(':')
    return f'{hours}ч {minutes}мин {seconds}сек'


def is_visit_long(visit, minutes=60):
    delta_time_minutes = get_duration(visit) / 60
    return delta_time_minutes > minutes
