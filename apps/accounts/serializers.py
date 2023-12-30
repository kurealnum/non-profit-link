from rest_framework import serializers

from .models import Org, OrgContactInfo, OrgInfo, OrgLocation


class OrgContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgContactInfo
        fields = "__all__"


class OrgInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgInfo
        fields = "__all__"


class OrgLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgLocation
        fields = "__all__"
