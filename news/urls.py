from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


story_list = views.StoryList.as_view()





urlpatterns = format_suffix_patterns([
   path('story/',views.CreateStoryView.as_view(),name='create-story'),
    path('story/<int:pk>/',views.StoryViewSet.as_view(),name='story'),
    path('story/<int:pk>/comments/',views.CommentViewSet.as_view(),name='comments'),
    path('comment/<int:pk>/',views.CommentDetail.as_view(),name='comment-detail'),
    path('stories/', story_list, name='story-list'),
    
])