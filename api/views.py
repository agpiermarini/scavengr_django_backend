from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from .models import User

class UsersView(viewsets.ViewSet):

    def create(self, request):
        try:
            queryset = User.objects.create(email=request.data['user']['email'], password=request.data['user']['password'])
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
