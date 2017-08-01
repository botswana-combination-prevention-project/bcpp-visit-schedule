from edc_map.mapper import Mapper


class TestMapper(Mapper):

    map_area = 'test_community'
    map_code = '01'
    mapper_model = 'bcpp_visit_schedule.testmodel'
    intervention = True


class TestMapper2(Mapper):

    map_area = 'test_community2'
    map_code = '02'
    mapper_model = 'bcpp_visit_schedule.testmodel'
    intervention = False
