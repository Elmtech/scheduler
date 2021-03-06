# -*- coding: utf-8 -*-

from django import template


register = template.Library()


@register.filter
def get_scheduler_date_fields(instance):
    # field that shouldn;t be displayed in template
    # ex.: exclude_fields = ['field_a', 'field_b', 'field_c']
    exclude_fields = ['id', 'field_a', ]
    instance.fields = [(field.verbose_name, field.value_to_string(instance))
                       for field in instance._meta.fields if field.name not in exclude_fields]
    return instance
