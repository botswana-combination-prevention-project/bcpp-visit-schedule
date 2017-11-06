from bcpp_community import is_intervention
from edc_visit_schedule.visit import Crf, FormsCollection

from edc_map.site_mappers import site_mappers


app_label = 'bcpp_subject'


class CrfsAhs(FormsCollection):

    @property
    def forms(self):
        # change according to intervention or not
        if is_intervention(site_mappers.current_map_area):
            forms = [crf for crf in self._forms
                     if crf.model not in [f'{app_label}.hivuntested']]
        else:
            forms = [crf for crf in self._forms
                     if crf.model not in [
                         f'{app_label}.tbsymptoms', f'{app_label}.hivuntested']]
        return forms


crfs_ahs = CrfsAhs(
    Crf(show_order=10, model=f'{app_label}.residencymobility', required=True),
    Crf(show_order=20, model=f'{app_label}.demographics', required=True),
    Crf(show_order=30, model=f'{app_label}.education', required=True),
    Crf(show_order=40, model=f'{app_label}.hivtestinghistory', required=True),
    Crf(show_order=50, model=f'{app_label}.hivtestreview', required=True),
    Crf(show_order=60, model=f'{app_label}.hivresultdocumentation',
        required=True),
    Crf(show_order=70, model=f'{app_label}.hivtested', required=True),
    Crf(show_order=85, model=f'{app_label}.hivcareadherence', required=True),
    Crf(show_order=90, model=f'{app_label}.sexualbehaviour', required=True),
    Crf(show_order=100, model=f'{app_label}.recentpartner', required=True),
    Crf(show_order=110, model=f'{app_label}.secondpartner', required=True),
    Crf(show_order=120, model=f'{app_label}.thirdpartner', required=True),
    Crf(show_order=140, model=f'{app_label}.hivmedicalcare', required=True),
    Crf(show_order=145, model=f'{app_label}.accesstocare', required=False),
    Crf(show_order=150, model=f'{app_label}.circumcision', required=True),
    Crf(show_order=160, model=f'{app_label}.circumcised', required=True),
    Crf(show_order=170, model=f'{app_label}.uncircumcised', required=True),
    Crf(show_order=180,
        model=f'{app_label}.reproductivehealth', required=True),
    Crf(show_order=210, model=f'{app_label}.medicaldiagnoses', required=True),
    Crf(show_order=215,
        model=f'{app_label}.hypertensioncardiovascular', required=True),
    Crf(show_order=220, model=f'{app_label}.heartattack', required=True),
    Crf(show_order=230, model=f'{app_label}.cancer', required=True),
    Crf(show_order=240, model=f'{app_label}.hivrelatedillness', required=True),
    Crf(show_order=250, model=f'{app_label}.tuberculosis', required=True),
    Crf(show_order=260, model=f'{app_label}.tbsymptoms', required=True),
    Crf(show_order=270, model=f'{app_label}.qualityoflife', required=True),
    Crf(show_order=280,
        model=f'{app_label}.resourceutilization', required=True),
    Crf(show_order=290, model=f'{app_label}.outpatientcare', required=True),
    Crf(show_order=300, model=f'{app_label}.ceaopd', required=True),
    Crf(show_order=310, model=f'{app_label}.hospitaladmission', required=True),
    Crf(show_order=320,
        model=f'{app_label}.hivhealthcarecosts', required=True),
    Crf(show_order=330, model=f'{app_label}.labourmarketwages', required=True),
    Crf(show_order=340, model=f'{app_label}.hivlinkagetocare', required=True),
    Crf(show_order=350, model=f'{app_label}.hivresult', required=True),
    Crf(show_order=360, model=f'{app_label}.elisahivresult',
        required=False, additional=True),
    Crf(show_order=370, model=f'{app_label}.pimacd4',
        required=False, additional=True),
    Crf(show_order=380, model=f'{app_label}.hicenrollment',
        required=False, additional=True),
    Crf(show_order=390, model=f'{app_label}.subjectreferral', required=True)
)
