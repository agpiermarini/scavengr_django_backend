from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import FoodSerializer, MealSerializer
from .models import Food, Meal

class UsersView(viewsets.ViewSet):

    def create(self, requeset):
        try:
            queryset = User.objects.create(email=request.data['user'['email'], password=request.data['user']['password'])
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialzer = UserSerializer(queryset, many=False)
        return Response(serializer.data)        
