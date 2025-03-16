# import time
from rest_framework import response, status
from rest_framework.views import APIView

# from core.tasks import sharedTask

# Create your views here.


class TaskView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def get(self, request, format=None):
        # sharedTask.delay()
        return response.Response(
            {"msg": "Helloworld"}, status=status.HTTP_200_OK
        )
