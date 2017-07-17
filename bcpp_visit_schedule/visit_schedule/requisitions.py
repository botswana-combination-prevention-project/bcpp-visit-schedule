from edc_visit_schedule.visit import Requisition, FormsCollection, Panel

RESEARCH_BLOOD_DRAW = 'Research Blood Draw'
MICROTUBE = 'Microtube'
VIRAL_LOAD = 'Viral Load'
ELISA = 'ELISA'

elisa_panel = Panel(name=ELISA)
microtube_panel = Panel(name=MICROTUBE)
rdb_panel = Panel(name=RESEARCH_BLOOD_DRAW)
viral_load_panel = Panel(name=VIRAL_LOAD)
venous_panel = Panel(name=VIRAL_LOAD)

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
