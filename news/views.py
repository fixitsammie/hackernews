from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CommentSerializer, StorySerializer, CommentTreeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Story,Comment

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .permissions import  IsWrittenByApi



class CreateStoryView(APIView):
    permission_classes = (IsWrittenByApi,)
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    def post(self, request, format=None):
        serializer = StorySerializer(data=request.data,context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoryViewSet(APIView):
    permission_classes = (IsWrittenByApi,)
    queryset = Story.objects.all()
    serializer_class = StorySerializer

    @classmethod
    def get_extra_actions(cls):
        return []
    """
    API endpoint that allows story to be posted and deleted.
    """

    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        story = self.get_object(pk)
        serializer = StorySerializer(story,context={'request': request})
        return Response(serializer.data)

    

    def put(self, request, pk, format=None):
        story = self.get_object(pk)
        self.check_object_permissions(request, story)
        serializer = StorySerializer(story, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        story = self.get_object(pk)
        self.check_object_permissions(request, story)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StoryList(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['text']
    #search_fields = ['text']
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']
    

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



class CommentViewSet(APIView):
    permission_classes = (IsWrittenByApi,)
    queryset = Comment.objects.all()
   

    @classmethod
    def get_extra_actions(cls):
        return []
    """
    Use story ID to retrieve Comments
    """

    def get_object(self, pk):
        """retrieve comment with with story object"""
        try:
            story  = Story.objects.get(pk=pk)
        except Story.DoesNotExist:
            raise Http404
        return Comment.objects.filter(news=story)
    
    def get_comment(self,pk):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
        return comment
        

    def get(self, request, pk, format=None):
        comments = self.get_comment(pk)
        serializer = CommentTreeSerializer(comments,many=True,context={'request': request})
        return Response(serializer.data)
    
    def list(self,request,pk,format=None):
        comments = self.get_object(pk)
        serializer = CommentTreeSerializer(comments,many=True,context={'request': request})
        return Response(serializer.data)




class CommentDetail(APIView):
    @classmethod
    def get_extra_actions(cls):
        return []
    """
    Use story ID to retrieve Comments
    """

    def get_object(self, pk):
        """retrieve comment with with story object"""
        try:
            comment  = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
        return comment
    

    def get(self, request, pk, format=None):
        comments = self.get_object(pk)
        #serializer = CommentTreeSerializer(comments,context={'request': request})
        serializer = CommentSerializer(comments,context={'request': request})        
        return Response(serializer.data)