# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class SchedulerDate(models.Model):
    field_a = models.DateField(verbose_name=_('תאריך לועזי'))
    field_b = models.CharField(verbose_name=_('יום בשבוע'), max_length=255, blank=True)
    field_c = models.CharField(verbose_name=_('פרשת'), max_length=255, blank=True)
    field_d = models.CharField(verbose_name=_('תאריך עברי'), max_length=255, blank=True)
    field_e = models.CharField(verbose_name=_('הערה'), max_length=255, blank=True)
    field_f = models.TimeField(verbose_name=_('משנה והלכה יומית'), null=True, blank=True)
    field_g = models.TimeField(verbose_name=_('שחרית מנין א'), null=True, blank=True)
    field_h = models.TimeField(verbose_name=_('שחרית מנין ב'), null=True, blank=True)
    field_i = models.TimeField(verbose_name=_('שעור בדף היומי'), null=True, blank=True)
    field_j = models.TimeField(verbose_name=_('שעור לנשים'), null=True, blank=True)
    field_k = models.TimeField(verbose_name=_('מנחה גדולה'), null=True, blank=True)
    field_l = models.TimeField(verbose_name=_('מנחה קטנה'), null=True, blank=True)
    field_m = models.CharField(verbose_name=_('שעור עין יעקב'), max_length=255, blank=True)
    field_n = models.TimeField(verbose_name=_('ערבית מנין א'), null=True, blank=True)
    field_o = models.CharField(verbose_name=_('הערה ב'), max_length=255, blank=True)
    field_p = models.CharField(verbose_name=_('לאחר ערבית שעור מפי הרב'), max_length=255, blank=True)
    field_q = models.TimeField(verbose_name=_("שעור גמ' מסכת יומא"), null=True, blank=True)
    field_r = models.TimeField(verbose_name=_('שעור בנביא ממו"ר הרב שליט"א'), null=True, blank=True)
    field_s = models.TimeField(verbose_name=_("ערבית מנין ב'"), null=True, blank=True)
    field_t = models.TimeField(verbose_name=_("שעור משניות מפי הרב מרדכי אדלשטיין"), null=True, blank=True)
    field_u = models.TimeField(verbose_name=_("הדלקת נרות"), null=True, blank=True)
    field_v = models.TimeField(verbose_name=_("שחרית"), null=True, blank=True)
    field_w = models.CharField(verbose_name=_('משנה יומית'), max_length=255, blank=True)
    field_x = models.TimeField(verbose_name=_("שעור הדף היומי"), null=True, blank=True)
    field_y = models.TimeField(verbose_name=_("מנחה"), null=True, blank=True)
    field_z = models.TimeField(verbose_name=_("ערבית וצאת השבת"), null=True, blank=True)

    def __str__(self):
        return self.field_a.strftime('%d-%m-%Y')
