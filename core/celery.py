import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

celery_app = Celery("core")

# Carregar configurações do Django corretamente
celery_app.config_from_object(settings, namespace="CELERY")

# Descobrir automaticamente as tarefas nos apps do Django
celery_app.autodiscover_tasks()
