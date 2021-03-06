from rest_framework import viewsets, status
from rest_framework.response import Response
from scavengerhunts.serializers import ScavengerHuntSerializer
from scavengerhunts.models import ScavengerHunt
from django.shortcuts import get_object_or_404


class ScavengerHuntView(viewsets.ViewSet):

    def index(self, request):
        queryset = ScavengerHunt.objects.all()
        serializer = ScavengerHuntSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def show(self, request, id):
        scavenger_hunt = get_object_or_404(ScavengerHunt, pk=id)
        serializer = ScavengerHuntSerializer(scavenger_hunt, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ScavengerHuntSerializer(data=request.data)
        if serializer.is_valid():
            scavenger_hunt = serializer.save(user=request.user)
            if scavenger_hunt:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, id):
        scavenger_hunt = get_object_or_404(ScavengerHunt, pk=id)
        serializer = ScavengerHuntSerializer(data=request.data)
        if serializer.is_valid():
            scavenger_hunt = serializer.update(instance=scavenger_hunt, validated_data=serializer.data)
            if scavenger_hunt:
                serializer = ScavengerHuntSerializer(scavenger_hunt, many=False)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id):
        get_object_or_404(ScavengerHunt, id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
