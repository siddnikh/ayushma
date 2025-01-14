from rest_framework import serializers

from ayushma.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "external_id",
            "title",
            "created_at",
            "modified_at",
            "description",
            "is_default",
        )
        read_only_fields = ("external_id", "created_at", "modified_at")


class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ProjectSerializer.Meta.fields + ("prompt",)
    
    def update(self, instance, validated_data):
        if validated_data.get("is_default", True):
            Project.objects.all().update(is_default=False)
        return super().update(instance, validated_data)
