import time

from django.utils import timezone
from config import celery_app

from .models import Task


@celery_app.task
def long_task():
    start_at = timezone.now()
    time.sleep(10)
    end_at = timezone.now()

    task = Task.objects.create(
        start_at=start_at,
        end_at=end_at,
    )
    return str(task)
