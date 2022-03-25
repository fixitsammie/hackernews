from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Story,Comment
from rest_framework_recursive.fields import RecursiveField

class StorySerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)
    id = serializers.ReadOnlyField()
    class Meta:
        model = Story
        fields = '__all__'

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ['hn_id','name' ]



class CommentTreeSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField()
    children = serializers.ListField(child=RecursiveField())

    class Meta:
        model = Comment
        fields = '__all__'
    