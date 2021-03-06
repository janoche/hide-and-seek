import os


BROKER_URL = os.environ.get('BROKER_URL')
BROKER_USE_SSL = os.environ.get('BROKER_USE_SSL', False)
CELERY_IMPORTS = ('worker',)
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ('json',)
CELERYD_FORCE_EXECV = True
CELERYD_MAX_TASKS_PER_CHILD = 1
