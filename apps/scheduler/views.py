# -*- coding: utf-8 -*-

from django.utils import timezone
from django.views.generic import ListView

from .models import SchedulerDate


class SchedulerHomeView(ListView):
    template_name = 'scheduler/home.html'
    context_object_name = 'scheduler_dates'

    def get_queryset(self):
        return SchedulerDate.objects.filter(field_a__gte=timezone.now().date())[:2]
