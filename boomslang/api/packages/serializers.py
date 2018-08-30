""""""

from packages.models import Build, Package, Version
from rest_framework import serializers


class PackageSerializer(serializers.ModelSerializer):
    """Serializer used to return the full data of a package."""

    class Meta:
        model = Package
        fields = (
            "id", "name", "team_owner", "user_owner",
            "license_type", "author", "summary", "description", "docs_url", "home_page",
            "package_url", "project_url", "bugtrack_url", "requires_dist",
            "is_public", "quality_check",
        )

    def validate_name(self, value):
        """IMPLEMENT ME"""
        return value

    def validate(self, validated_data):
        """IMPLEMENT ME"""
        return validated_data

    def create(self, validated_data):
        """IMPLEMENT ME"""
        user = self.context["request"].user
        package = Package(**validated_data)
        package.save()
        return package


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ()


class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ()
