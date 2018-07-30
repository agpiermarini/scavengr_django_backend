from rest_framework import viewsets, status
from rest_framework.response import Response
from currentscavengerhunts.serializers import CurrentScavengerHuntSerializer
from scavengerhunts.models import ScavengerHunt
from django.shortcuts import get_object_or_404

class CurrentScavengerHuntView(viewsets.ViewSet):

    def create(self, request):
        scavenger_hunt = get_object_or_404(ScavengerHunt, id=request.data["scavenger_hunt_id"])
        serializer = CurrentScavengerHuntSerializer(data=request.data)
        if serializer.is_valid():
            current_scavenger_hunt = serializer.save(user=request.user, scavenger_hunt=scavenger_hunt)
            if current_scavenger_hunt:
                return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
