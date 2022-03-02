from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Story,Comment


class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ['url', 'hacker_news_item', 'time', 'url']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['hn_id','name' ]