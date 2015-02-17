from django.contrib.auth.models import User
from rest_framework import serializers
from data_api.models import DoomMap


class DoomMapSerializer(serializers.Serializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='highlight_details', format='html')
    class Meta:
        fields = ('episode', 'name', 'cheats', 'map')

    episode= serializers.IntegerField(max_value=1000)
    name = serializers.CharField(max_length=200)
    cheats = serializers.ListField(
        child=serializers.CharField(max_length=200)
    )
    map=serializers.IntegerField(max_value=100)

class ThreadSerializer(serializers.Serializer):
    class Meta:
        fields = ('forum_name', 'subject', 'answered', 'last_post_datetime', 'replies', 'tags', 'views')

    forum_name = serializers.CharField(max_length=200)
    subject = serializers.CharField(max_length=200)
    answered = serializers.IntegerField(max_value=1000)
    last_post_datetime = serializers.CharField(max_length=200)
    replies = serializers.IntegerField(max_value=1000)
    tags = serializers.ListField(child=serializers.CharField(max_length=200))
    views = serializers.IntegerField(max_value=1000)