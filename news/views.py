from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CommentSerializer, StorySerializer
from .models import Story


class StoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows story to be viewed or edited.
    """
    queryset = Story.objects.all().order_by('-date_joined')
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated]

