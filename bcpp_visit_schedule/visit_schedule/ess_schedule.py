from edc_visit_schedule.schedule import Schedule
from edc_visit_schedule.visit import Visit

from ..constants import E0
from .crfs_ess import crfs_ess
from .requisitions import requisitions

app_label = 'bcpp_subject'

# schedule for new participants
ess_schedule = Schedule(
    name='ess_schedule',
    title='ESS',
    enrollment_model=f'{app_label}.enrollmentess',
    disenrollment_model=f'{app_label}.disenrollmentess')

ess_visit = Visit(
    code=E0,
    title='End-of-study Household Survey',
    timepoint=0,
    base_interval=0,
    requisitions=requisitions.forms,
    crfs=crfs_ess.forms)

ess_schedule.add_visit(visit=ess_visit)
