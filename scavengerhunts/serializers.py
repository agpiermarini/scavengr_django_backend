
from rest_framework import serializers
from .models import ScavengerHunt

class ScavengerHuntSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=250)
    username = serializers.ReadOnlyField()

    def create(self, validated_data):
        return ScavengerHunt.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.save()
        return instance

    class Meta:
        model = ScavengerHunt
        fields = ('id', 'name', 'description', 'user_id', 'username')
