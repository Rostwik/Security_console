from datacenter.models import Visit
from django.shortcuts import render

from visit_tools import is_visit_long, get_duration, format_duration


def storage_information_view(request):
    non_closed_visits = []
    suspect_visits = []
    not_ended_visit = Visit.objects.filter(leaved_at__isnull=True)
    all_visits = Visit.objects.all()

    for visit in all_visits:
        if visit.entered_at and visit.leaved_at:
            if is_visit_long(visit):
                suspect_visits.append(visit)

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
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
