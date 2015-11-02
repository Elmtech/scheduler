# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import codecs

from django import forms
from django.utils.translation import ugettext_lazy as _


class UploadCsvData(forms.Form):

    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.content_type not in ['text/csv']:
            raise forms.ValidationError(_('Only csv files can be uploaded'))

        return file
