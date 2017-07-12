from dateutil.relativedelta import relativedelta

from edc_visit_schedule.constants import YEARS
from edc_visit_schedule.schedule import Schedule
from edc_visit_schedule.visit import Visit

from ..constants import T1, T2
from .crfs_ahs import crfs_ahs
from .requisitions import requisitions

app_label = 'bcpp_subject'

ahs_schedule = Schedule(
    name='ahs_schedule',
    title='AHS',
    enrollment_model=f'{app_label}.enrollmentahs',
    disenrollment_model=f'{app_label}.disenrollmentahs',)

ahs_visit1 = Visit(
    code=T1,
    title='1st Annual Survey',
    timepoint=1,
    rbase=relativedelta(years=1),
    rlower=relativedelta(years=1),
    rupper=relativedelta(years=2),
    base_interval_unit=YEARS,
    requisitions=requisitions.forms,
    crfs=crfs_ahs.forms)

ahs_visit2 = Visit(
    code=T2,
    title='2nd Annual Survey',
    timepoint=2,
    rbase=relativedelta(years=2),
    rlower=relativedelta(years=2),
    rupper=relativedelta(years=3),
    base_interval_unit=YEARS,
    requisitions=requisitions.forms,
    crfs=crfs_ahs.forms)

ahs_schedule.add_visit(visit=ahs_visit1)
ahs_schedule.add_visit(visit=ahs_visit2)
