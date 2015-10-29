# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import SchedulerDate


@admin.register(SchedulerDate)
class SchedulerDateAdmin(admin.ModelAdmin):
    pass
