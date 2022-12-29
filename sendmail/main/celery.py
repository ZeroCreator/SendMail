import os
from celery import Celery
# from celery.shedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sendmail.settings')

app = Celery('sendmail')
# app.conf.update('django.conf:settings', namespace='CELERY')
# app.autodiscover_task()

# celery beat task

# app.conf.beat_shedule = {
#     'send-spam-every10-minute': {
#         'task': 'main.tasks.send_beat_email',
#         'schedule': crontab(minute='*/10'),
#     },
# }
