from rest_framework import serializers

from ayushma.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "full_name",
        )


class UserCreateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "full_name",
            "password",
            "email",
        )


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "external_id",
            "username",
            "full_name",
            "email",
            "allow_key",
            "is_staff",
        )
        read_only_fields = ("external_id", "email", "username", "allow_key", "is_staff")

    def update(self, instance, validated_data):
        if password := validated_data.pop("password", None):
            instance.set_password(password)
        return super().update(instance, validated_data)
