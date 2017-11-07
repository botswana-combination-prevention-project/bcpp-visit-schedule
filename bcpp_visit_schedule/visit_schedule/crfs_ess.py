from edc_visit_schedule.visit import Crf, FormsCollection

app_label = 'bcpp_subject'


class CrfsEss(FormsCollection):
    pass


crfs_ess = CrfsEss(
    Crf(show_order=10, model=f'{app_label}.residencymobility', required=True),
    Crf(show_order=30, model=f'{app_label}.immigrationstatus', required=False),
    Crf(show_order=35, model=f'{app_label}.demographics', required=True),
    Crf(show_order=37, model=f'{app_label}.education', required=True),
    Crf(show_order=40, model=f'{app_label}.hivtestinghistory', required=True),
    Crf(show_order=50, model=f'{app_label}.hivtestreview', required=True),
    Crf(show_order=60, model=f'{app_label}.hivresultdocumentation',
        required=True),
    Crf(show_order=70, model=f'{app_label}.hivtested', required=True),
    Crf(show_order=80, model=f'{app_label}.hivuntested', NOT_required=True),
    Crf(show_order=85, model=f'{app_label}.hivcareadherence', required=True),
    Crf(show_order=90, model=f'{app_label}.sexualbehaviour', required=True),
    Crf(show_order=100, model=f'{app_label}.recentpartner', required=True),
    Crf(show_order=110, model=f'{app_label}.secondpartner', required=True),
    Crf(show_order=120, model=f'{app_label}.thirdpartner', required=True),
    Crf(show_order=130, model=f'{app_label}.substanceuse', required=True),
    Crf(show_order=140, model=f'{app_label}.hivmedicalcare', required=True),
    Crf(show_order=145, model=f'{app_label}.accesstocare', required=False),
    Crf(show_order=150, model=f'{app_label}.circumcision', required=True),
    Crf(show_order=160, model=f'{app_label}.circumcised', required=True),
    Crf(show_order=170, model=f'{app_label}.uncircumcised', required=True),
    Crf(show_order=180,
        model=f'{app_label}.reproductivehealth', required=True),
    Crf(show_order=190, model=f'{app_label}.pregnancy', required=True),
    Crf(show_order=200, model=f'{app_label}.nonpregnancy', required=True),
    Crf(show_order=210, model=f'{app_label}.medicaldiagnoses', required=True),
    Crf(show_order=220, model=f'{app_label}.heartattack', required=True),
    Crf(show_order=230, model=f'{app_label}.cancer', required=True),
    Crf(show_order=240, model=f'{app_label}.hivrelatedillness', required=True),
    Crf(show_order=250, model=f'{app_label}.tuberculosis', required=True),
    Crf(show_order=260, model=f'{app_label}.tbsymptoms', required=True),
    # Crf(show_order=330, model=f'{app_label}.hivlinkagetocare',
    # required=True),
    Crf(show_order=340, model=f'{app_label}.hivresult', required=True),
    Crf(show_order=350, model=f'{app_label}.elisahivresult',
        required=False, additional=True),
    Crf(show_order=360, model=f'{app_label}.pimacd4',
        required=False, additional=True),
    Crf(show_order=370, model=f'{app_label}.subjectreferral', required=True),
)
