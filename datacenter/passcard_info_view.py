from django.http import Http404
from django.shortcuts import render

from datacenter.models import Visit, Passcard
from visit_tools import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    try:
        passcard = Passcard.objects.get(passcode=passcode)
    except Passcard.DoesNotExist:
        raise Http404
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
