from rest_framework import viewsets, status
from rest_framework.response import Response
from scavengerhunts.serializers import ScavengerHuntSerializer
from scavengerhunts.models import ScavengerHunt

class ScavengerHuntView(viewsets.ViewSet):

    def create(self, request):
        serializer = ScavengerHuntSerializer(data=request.data)
        if serializer.is_valid():
            scavenger_hunt = serializer.save(user=request.user)
            if scavenger_hunt:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
