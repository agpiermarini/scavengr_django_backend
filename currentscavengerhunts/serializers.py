from rest_framework import serializers
from currentscavengerhunts.models import CurrentScavengerHunt

class CurrentScavengerHuntSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return CurrentScavengerHunt.objects.get_or_create(**validated_data)

    class Meta:
        model = CurrentScavengerHunt
        fields = ('scavenger_hunt_id', 'user_id', 'created_at', 'name', 'description')
