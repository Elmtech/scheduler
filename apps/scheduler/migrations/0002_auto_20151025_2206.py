# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulerdate',
            name='field_a',
            field=models.DateField(verbose_name='תאריך לועזי', unique=True),
        ),
    ]
