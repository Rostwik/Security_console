import datetime
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from project.settings import TIME_ZONE
import pytz


def is_visit_long(visit, minutes=600):
    moscow_time_zone = pytz.timezone(TIME_ZONE)
    visit_enter_time = localtime(value=visit.entered_at, timezone=moscow_time_zone)
    visit_leave_time = localtime(value=visit.leaved_at, timezone=moscow_time_zone)
    delta_time_minutes = (visit_leave_time - visit_enter_time).total_seconds() / 60
    if delta_time_minutes > minutes:
        return True
    return False


def get_duration(visit):
    moscow_time_zone = pytz.timezone(TIME_ZONE)

    visit_enter_time = localtime(value=visit.entered_at, timezone=moscow_time_zone)
    time_now = localtime()
    delta_time = time_now - visit_enter_time
    delta_time_seconds = delta_time.total_seconds()
    return delta_time_seconds


def format_duration(duration):
    hours, minutes, seconds = str(datetime.timedelta(seconds=int(duration))).split(':')
    return f'{hours}ч {minutes}мин {seconds}сек'


def storage_information_view(request):
    non_closed_visits = []
    suspect_visits = []
    not_ended_visit = Visit.objects.filter(leaved_at__isnull=True)
    all_visits = Visit.objects.all()

    for visit in all_visits:
        if visit.entered_at and visit.leaved_at:
            if is_visit_long(visit):
                suspect_visits.append(visit)
    print('Визиты дольше 10мин:', suspect_visits)

    for visit in not_ended_visit:
        duration = get_duration(visit)

        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': format_duration(duration)
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
