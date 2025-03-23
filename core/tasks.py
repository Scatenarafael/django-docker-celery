import logging
import time

from celery import shared_task

# from .celery import app

logger = logging.getLogger("conections_logger")


@shared_task(name="core.add")  # Defina um nome explícito
def add(x, y):
    logger.debug("Adding...")
    return x + y


@shared_task(name="core.write")  # Defina um nome explícito
def write():
    logger.debug("Adding...")
    return "Helloworld"


@shared_task(queue="emails", name="core.send_email")
def send_email(email):
    logger.debug("Sending email...")
    """Simula o envio de um e-mail."""
    print(f"📨 Enviando e-mail para {email}...")
    time.sleep(2)  # Simula o tempo de envio do e-mail
    return f"E-mail enviado para {email}!"
