from django.db import models
from django.utils.timezone import localtime

import pytz

from project.settings import TIME_ZONE


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

    def get_visit_localtime(self):
        moscow_time_zone = pytz.timezone(TIME_ZONE)
        localtime_entered_at_visit = localtime(value=self.entered_at, timezone=moscow_time_zone)
        localtime_leaved_at_visit = localtime(value=self.leaved_at, timezone=moscow_time_zone)
        return localtime_entered_at_visit, localtime_leaved_at_visit
