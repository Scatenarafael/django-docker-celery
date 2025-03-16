from celery import shared_task


@shared_task
def sharedTask():
    print("hellowWorld")
    return
