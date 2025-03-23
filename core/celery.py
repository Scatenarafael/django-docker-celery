import os

from celery import Celery
from celery.schedules import crontab
from celery.signals import setup_logging  # noqa
from django.apps import apps  # Importação correta
from kombu import Queue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")


# Definição das filas
app.conf.task_queues = (Queue("emails"),)  # Fila para envio de e-mails

# Definição de roteamento automático
app.conf.task_routes = {
    "core.send_email": {"queue": "emails"},
}


app.conf.beat_schedule = {
    "add-every-minute": {
        "task": "core.add",
        "schedule": crontab(minute="*/5"),
        "args": (16, 16),
    },
    "write-every-minute": {
        "task": "core.write",
        "schedule": crontab(minute="*/10"),
    },
    "send-email-every-minute": {
        "task": "core.send_email",
        "schedule": crontab(minute="*/15"),
        "args": ["rafascatena@gmail.com"],
    },
}

# app.conf.timezone = "UTC"


@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig  # noqa

    from django.conf import settings  # noqa

    dictConfig(settings.LOGGING)


# Descobre tasks automaticamente dentro de todos os apps Django
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
