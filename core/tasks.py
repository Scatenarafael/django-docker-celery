import logging
import time

from celery import shared_task

# from core.settings import BASE_DIR

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


@shared_task(queue="files", name="core.move_files")
def move_files(filename, dir):
    logger.info(f"Moving file... {dir}, {filename}")
    time.sleep(20)
    # try:
    #     with open(f"{dir}/{filename}", "r", encoding="latin1") as file:
    #         file_content = file.read()
    #     logger.info(f"File {filename} successfully read!")
    # except FileNotFoundError:
    #     logger.error(f"File not found: {dir}/{filename}")
    #     return "File not found!"
    # except Exception as e:
    #     logger.error(f"An error occurred: {e}")
    #     return "An error occurred!"
    # try:
    #     logger.info(f"Moving {filename} to {BASE_DIR}/destination...")
    #     with open(f"{BASE_DIR}/destination/{filename}", "w") as file:
    #         file.write(file_content)
    # except FileNotFoundError:
    #     logger.error(f"Directory not found: {BASE_DIR}/destination")
    #     return "Directory not found!"
    # except Exception as e:
    #     logger.error(f"An error occurred: {e}")
    # logger.info(f"File {filename} successfully moved!")
    # return "File moved!"
