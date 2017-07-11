from django.conf import settings

if settings.APP_NAME == 'bcpp_visit_schedule':
    from .tests.models import TestModel
