from rest_framework import viewsets, status
from rest_framework.response import Response
from users.serializers import UserSerializer
from scavengerhunts.models import ScavengerHunt
from scavengerhunts.serializers import ScavengerHuntSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny

class UserCreateView(viewsets.ViewSet):
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

class UserScavengerHuntView(viewsets.ViewSet):

    def index(self, request, username):
        queryset = User.objects.get(username=username).scavengerhunt_set.all()
        serializer = ScavengerHuntSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'token': token.key,
        })
