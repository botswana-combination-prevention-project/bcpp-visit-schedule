from edc_visit_schedule.schedule import Schedule
from edc_visit_schedule.visit import Visit

from ..constants import A0
from .crfs_ess import crfs_ess
from .requisitions import requisitions

app_label = 'bcpp_subject'

ano_schedule = Schedule(
    name='ano_schedule',
    title='Anonymous',
    enrollment_model=f'{app_label}.enrollmentano',
    disenrollment_model=f'{app_label}.disenrollmentano')

ano_visit = Visit(
    code=A0,
    title='Anonymous Survey',
    timepoint=0,
    base_interval=0,
    requisitions=requisitions.forms,
    crfs=crfs_ess.forms)

ano_schedule.add_visit(visit=ano_visit)
