# -*- coding: utf-8 -*-
from django.db import migrations, models
from django.core import management


def load_admin_fixture(apps, schema_editor):
    management.call_command('loaddata', 'admin_fixture.json')


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchedulerDate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('field_a', models.DateField(verbose_name='תאריך לועזי')),
                ('field_b', models.CharField(blank=True, max_length=255, verbose_name='יום בשבוע')),
                ('field_c', models.CharField(blank=True, max_length=255, verbose_name='פרשת')),
                ('field_d', models.CharField(blank=True, max_length=255, verbose_name='תאריך עברי')),
                ('field_e', models.CharField(blank=True, max_length=255, verbose_name='הערה')),
                ('field_f', models.TimeField(blank=True, null=True, verbose_name='משנה והלכה יומית')),
                ('field_g', models.TimeField(blank=True, null=True, verbose_name='שחרית מנין א')),
                ('field_h', models.TimeField(blank=True, null=True, verbose_name='שחרית מנין ב')),
                ('field_i', models.TimeField(blank=True, null=True, verbose_name='שעור בדף היומי')),
                ('field_j', models.TimeField(blank=True, null=True, verbose_name='שעור לנשים')),
                ('field_k', models.TimeField(blank=True, null=True, verbose_name='מנחה גדולה')),
                ('field_l', models.TimeField(blank=True, null=True, verbose_name='מנחה קטנה')),
                ('field_m', models.CharField(blank=True, max_length=255, verbose_name='שעור עין יעקב')),
                ('field_n', models.TimeField(blank=True, null=True, verbose_name='ערבית מנין א')),
                ('field_o', models.CharField(blank=True, max_length=255, verbose_name='הערה ב')),
                ('field_p', models.CharField(blank=True, max_length=255, verbose_name='לאחר ערבית שעור מפי הרב')),
                ('field_q', models.TimeField(blank=True, null=True, verbose_name="שעור גמ' מסכת יומא")),
                ('field_r', models.TimeField(blank=True, null=True, verbose_name='שעור בנביא ממו"ר הרב שליט"א')),
                ('field_s', models.TimeField(blank=True, null=True, verbose_name="ערבית מנין ב'")),
                ('field_t', models.TimeField(blank=True, null=True, verbose_name='שעור משניות מפי הרב מרדכי אדלשטיין')),
                ('field_u', models.TimeField(blank=True, null=True, verbose_name='הדלקת נרות')),
                ('field_v', models.TimeField(blank=True, null=True, verbose_name='שחרית')),
                ('field_w', models.CharField(blank=True, max_length=255, verbose_name='משנה יומית')),
                ('field_x', models.TimeField(blank=True, null=True, verbose_name='שעור הדף היומי')),
                ('field_y', models.TimeField(blank=True, null=True, verbose_name='מנחה')),
                ('field_z', models.TimeField(blank=True, null=True, verbose_name='ערבית וצאת השבת')),
            ],
        ),
        migrations.RunPython(load_admin_fixture),
    ]
