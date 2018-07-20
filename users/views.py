from rest_framework import viewsets, status
from rest_framework.response import Response
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserView(viewsets.ViewSet):

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                json['token'] = Token.objects.create(user=user).key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
