from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Story

class StoryTests(APITestCase):
    def test_create_hn_story(self):
        """
        HN story has hacker_news_item set to true
        Ensure we can create a new account object.
        """
        url = reverse('create-story')
        data = {'name': 'New story','hacker_news_item':True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Story.objects.count(), 1)
        self.assertEqual(Story.objects.get().name, 'DabApps')

    def test_create_api_story(self):
        """
        HN story has hacker_news_item set to true
        Ensure we can create a new account object.
        """
        url = reverse('create-story')
        data = {'name': 'New story','hacker_news_item':False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Story.objects.count(), 1)
        self.assertEqual(Story.objects.get().name, 'DabApps')

    def test_update_hn_story(self):
        """Ensure that HN story cannot be updated"""
        url = reverse('story')
        data = {'name': 'New story', 'hacker_news_item': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_api_story(self):
        """Ensure that API story can be updated"""
        url = reverse('create-story')
        data = {'name': 'New story', 'hacker_news_item': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


