from rest_framework import serializers


class RequestDataSerializer(serializers.Serializer):
    num = serializers.IntegerField()
    gubn = serializers.CharField(max_length=2)
    mea_ymd = serializers.CharField(max_length=10)
    mea_ymd2 = serializers.CharField(max_length=10)
