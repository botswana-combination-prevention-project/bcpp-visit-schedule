from edc_visit_schedule.schedule import Schedule
from edc_visit_schedule.visit import Visit

from ..constants import T0
from .crfs_bhs import crfs_bhs
from .requisitions import requisitions

app_label = 'bcpp_subject'

bhs_schedule = Schedule(
    name='bhs_schedule',
    title='BHS',
    enrollment_model=f'{app_label}.enrollmentbhs',
    disenrollment_model=f'{app_label}.disenrollmentbhs',)

bhs_visit = Visit(
    code=T0,
    title='Baseline Survey',
    timepoint=0,
    base_interval=0,
    requisitions=requisitions.forms,
    crfs=crfs_bhs.forms)

bhs_schedule.add_visit(visit=bhs_visit)
