from rest_framework import viewsets, status
from rest_framework.response import Response
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny


class UserView(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                json['token'] = Token.objects.get(user=user).key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
