# -*- coding: utf-8 -*-

import csv

from datetime import datetime
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, FormView

from .models import SchedulerDate
from .forms import UploadCsvData


class SchedulerHomeView(ListView):
    template_name = 'scheduler/home.html'
    context_object_name = 'scheduler_dates'

    def get_queryset(self):
        return SchedulerDate.objects.filter(field_a__gte=datetime.now().date())[:2]


class UploadCsvDataView(FormView):
    template_name = 'scheduler/upload_csv.html'
    form_class = UploadCsvData
    success_url = reverse_lazy('scheduler:home')

    def form_valid(self, form):
        rows = csv.reader(form.cleaned_data['file'].read().decode('utf-8').splitlines())
        SchedulerDate.create_from_rows(rows)
        return super(UploadCsvDataView, self).form_valid(form)
