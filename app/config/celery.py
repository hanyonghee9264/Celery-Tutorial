import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
# bing=True 옵션을 주게 되면
# 아래 함수의 인자에 self가 추가됨 ==> 'self'는 관용적으로 쓰임
# 이 앱의 실행시켰을때에 대한 정보가 담겨져옴
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
