from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from cride.users.serializers.users import UserLoginSerializer, UserModelSerializer


class UserLoginAPIView(APIView):

    def post(self, request, *args, **kwargs):

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print("antes de save")
        user, token = serializer.save()
        #Acá ya llega una instancia de la clase model.User
        print("despues de save")
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)