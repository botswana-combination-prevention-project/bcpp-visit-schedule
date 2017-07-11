from django.test.utils import override_settings
from django.test import TestCase, tag

from edc_map.site_mappers import site_mappers
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from ..visit_schedule import visit_schedule_bhs, visit_schedule_ahs
from ..visit_schedule.crfs_ahs import crfs_ahs
from ..visit_schedule import visit_schedule_ano, visit_schedule_ess
from .mappers import TestMapper, TestMapper2


class TestVisitSchedule(TestCase):

    def setUp(self):
        site_mappers.registry = {}
        site_mappers.register(TestMapper)

    @override_settings(CURRENT_MAP_AREA='test_community')
    def test_ahs_in_intervention(self):
        """ Asserts difference in the CRF list between default list
        and AHS intervention map_area.
        """
        self.assertTrue(site_mappers.registry['test_community'].intervention)
        for crf in crfs_ahs.forms:
            self.assertNotIn(crf.model, ['bcpp_subject.hivuntested'])

    @override_settings(CURRENT_MAP_AREA='test_community2')
    def test_ahs_in_non_intervention(self):
        """Asserts difference in the CRF list between default list
        and AHS intervention map_area.
        """
        site_mappers._current_map_area = 'test_community2'
        site_mappers.registry = {}
        site_mappers.register(TestMapper2)
        self.assertFalse(site_mappers.registry['test_community2'].intervention)
        for crf in crfs_ahs.forms:
            self.assertNotIn(crf.model, ['bcpp_subject.tbsymptoms',
                                         'bcpp_subject.hivuntested'])

    def test_visit_schedule_register1(self):
        site_visit_schedules._registry = {}
        site_visit_schedules.register(visit_schedule_bhs)

    def test_visit_schedule_register2(self):
        site_visit_schedules._registry = {}
        site_visit_schedules.register(visit_schedule_ahs)

    def test_visit_schedule_register3(self):
        site_visit_schedules._registry = {}
        site_visit_schedules.register(visit_schedule_ano)

    def test_visit_schedule_register4(self):
        site_visit_schedules._registry = {}
        site_visit_schedules.register(visit_schedule_ess)

    def test_imports_all(self):
        site_visit_schedules.autodiscover(apps=['bcpp_visit_schedule'])
        self.assertEqual(
            len(list(site_visit_schedules.registry)), 4)
