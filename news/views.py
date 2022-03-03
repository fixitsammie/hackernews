from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CommentSerializer, StorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Story

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .permissions import  IsWrittenByApi


class StoryViewSet(APIView):
    permission_classes = (IsWrittenByApi,)
    """
    API endpoint that allows story to be posted and deleted.
    """

    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        serializer = StorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        story = self.get_object(pk)
        self.check_object_permissions(request, story)
        serializer = StorySerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        story = self.get_object(pk)
        self.check_object_permissions(request, story)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoryList(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['text']
    search_fields = ['text']
