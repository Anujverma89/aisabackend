from rest_framework import serializers

class memeberSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    post = serializers.CharField(max_length=100)
    branch = serializers.CharField(max_length=100)
    year = serializers.CharField(max_length=200)
    contact = serializers.CharField(max_length=10)
    image = serializers.ImageField()


class faqSerializer(serializers.Serializer):
    quesiton = serializers.CharField()
    answer = serializers.CharField()


class noticeSerializer(serializers.Serializer):
    heading = serializers.CharField(max_length=200)
    url = serializers.URLField()
    description = serializers.CharField()
    image = serializers.FileField()

class eventSerializer(serializers.Serializer):
    eventName = serializers.CharField(max_length=100)
    eventDesc = serializers.CharField()
    eventImage = serializers.FileField()
    eventType = serializers.CharField(max_length=200)

class gallerySerializer(serializers.Serializer):
    eventName = eventSerializer()
    galleryImage = serializers.FileField()
    eventName = serializers.CharField(max_length=100)

class blogSerializer(serializers.Serializer):
    heading = serializers.CharField(max_length=200)
    decs = serializers.CharField()
    link = serializers.URLField()
    authorName = serializers.StringRelatedField()