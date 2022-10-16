# DJANGO REST FRAMEWORK -- https://www.django-rest-framework.org/

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserAccount
from .serializer import UserAccountSerializer


class ListUsersAPIView(APIView):

    serializer_class = UserAccountSerializer

    def get(self, request: Request) -> Response:
        try:
            list_of_users = UserAccount.objects.all()
            serializer = self.serializer_class(list_of_users, many=True)

            response = {
                "status": "success",
                "data": serializer.data,
            }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
