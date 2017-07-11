from edc_visit_schedule.visit import Requisition, FormsCollection

from bcpp_labs.labs import rdb_panel, microtube_panel, viral_load_panel
from bcpp_labs.labs import venous_panel, elisa_panel


app_label = 'bcpp_subject'

requisitions = FormsCollection(
    Requisition(
        show_order=10, model=f'{app_label}.subjectrequisition',
        panel=rdb_panel, required=False, additional=False),
    Requisition(
        show_order=20, model=f'{app_label}.subjectrequisition',
        panel=viral_load_panel, required=False, additional=False),
    Requisition(
        show_order=30, model=f'{app_label}.subjectrequisition',
        panel=microtube_panel, required=False, additional=False),
    Requisition(
        show_order=40, model=f'{app_label}.subjectrequisition',
        panel=venous_panel, required=False, additional=False),
    Requisition(
        show_order=50, model=f'{app_label}.subjectrequisition',
        panel=elisa_panel, required=False, additional=False)
)
