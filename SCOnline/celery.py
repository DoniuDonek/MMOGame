from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SCOnline.settings')

app = Celery('SCOnline')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

CELERY_BEAT_SCHEDULE = {
    'collect-resources-every-10-seconds': {
        'task': 'units.tasks.collect_resources',
        'schedule': timedelta(seconds=10),
    },
}
