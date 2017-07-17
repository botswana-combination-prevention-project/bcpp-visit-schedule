import sys

from django.core.management.color import color_style

from edc_map.site_mappers import site_mappers
from edc_visit_schedule.visit_schedule import VisitSchedule

from .ahs_schedule import ahs_schedule
from .ano_schedule import ano_schedule
from .bhs_schedule import bhs_schedule
from .ess_schedule import ess_schedule

style = color_style()

app_label = 'bcpp_subject'

try:
    map_area = site_mappers.current_map_area
except AttributeError as e:
    sys.stdout.write(style.ERROR(
        '  * ERROR: visit schedule requires the current map area. '
        'Either the site mapper is not set or the current map area '
        'is not a valid \'community\'.\n    Got {} ({})\n'.format(
            site_mappers.current_map_area, str(e))))


visit_schedule_bhs = VisitSchedule(
    name='visit_schedule_bhs',
    verbose_name='BCPP Baseline Survey',
    app_label=app_label,
    enrollment_model=f'{app_label}.enrollmentbhs',
    disenrollment_model=f'{app_label}.disenrollmentbhs',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy',
    previous_visit_schedule=None,
)
visit_schedule_bhs.add_schedule(bhs_schedule)

visit_schedule_ahs = VisitSchedule(
    name='visit_schedule_ahs',
    verbose_name='BCPP Annual Surveys',
    app_label=app_label,
    enrollment_model=f'{app_label}.enrollmentahs',
    disenrollment_model=f'{app_label}.disenrollmentahs',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy',
    previous_visit_schedule=visit_schedule_bhs,
)
visit_schedule_ahs.add_schedule(ahs_schedule)

visit_schedule_ess = VisitSchedule(
    name='visit_schedule_ess',
    verbose_name='BCPP ESS Survey',
    app_label=app_label,
    enrollment_model=f'{app_label}.enrollmentess',
    disenrollment_model=f'{app_label}.disenrollmentess',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy',
    previous_visit_schedule=None,
)
visit_schedule_ess.add_schedule(ess_schedule)


visit_schedule_ano = VisitSchedule(
    name='visit_schedule_ano',
    verbose_name='BCPP Anonymous Survey',
    app_label=app_label,
    enrollment_model=f'{app_label}.enrollmentano',
    disenrollment_model=f'{app_label}.disenrollmentano',
    visit_model=f'{app_label}.subjectvisit',
    offstudy_model=f'{app_label}.subjectoffstudy',
    previous_visit_schedule=None,
)
visit_schedule_ano.add_schedule(ano_schedule)
