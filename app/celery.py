import os
from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.config.beat_schedule = {
    'get_joke_3s': {
        'task': 'jokes.tasks.get_joke',
        'schedule': 3.0
    }
}

app.autodiscover_tasks()