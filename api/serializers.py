from rest_framework import serializers


class RequestDataSerializer(serializers.Serializer):
    num = serializers.IntegerField()
    gubn = serializers.CharField(max_length=2)
    mea_ymd = serializers.CharField(max_length=10)
    mea_ymd2 = serializers.CharField(max_length=10)


class RequestAlarmSerializer(serializers.Serializer):
    level = serializers.IntegerField()
    email = serializers.CharField(max_length=100)
    minutes = serializers.IntegerField()
    gubn = serializers.CharField(max_length=2)
    gu_name = serializers.CharField(max_length=5)
