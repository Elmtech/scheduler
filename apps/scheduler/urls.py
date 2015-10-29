# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url
from .views import SchedulerHomeView


urlpatterns = [
    url(r'^$', SchedulerHomeView.as_view(), name='home'),
]
