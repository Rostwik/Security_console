from django.shortcuts import render

import datetime

from datacenter.models import Visit, Passcard


def get_duration(visit):
    visit_enter_time, visit_leave_time = visit.localtime_visit()
    delta_time = visit_leave_time - visit_enter_time
    delta_time_seconds = delta_time.total_seconds()
    return delta_time_seconds


def format_duration(duration):
    hours, minutes, seconds = str(datetime.timedelta(seconds=int(duration))).split(':')
    return f'{hours}ч {minutes}мин {seconds}сек'


def is_visit_long(visit, minutes=60):
    visit_enter_time, visit_leave_time = visit.localtime_visit()
    delta_time_minutes = (visit_leave_time - visit_enter_time).total_seconds() / 60
    return delta_time_minutes > minutes


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    try:
        passcard = Passcard.objects.get(passcode=passcode)
    except Passcard.DoesNotExist:
        print("Объект не найден.")
    else:
        all_visits = Visit.objects.filter(passcard=passcard)

        for visit in all_visits:
            if visit.entered_at and visit.leaved_at:
                duration_visit = get_duration(visit)

                this_passcard_visits.append(
                    {
                        'entered_at': visit.entered_at,
                        'duration': format_duration(duration_visit),
                        'is_strange': is_visit_long(visit)
                    },
                )

        context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits
        }
        return render(request, 'passcard_info.html', context)
