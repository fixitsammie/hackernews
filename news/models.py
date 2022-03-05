from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
from datetime import datetime


class Story(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    score = models.IntegerField()
    hacker_news_item = models.BooleanField()
    creator = models.CharField(max_length=1000)
    text = models.CharField(max_length=2000)
    hn_id = models.CharField(max_length=200,blank=True)
    url = models.CharField(max_length=2000)
    type = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    hacker_news_time = models.DateTimeField()

    def __str__(self):
          return self.text

    

    def save(self, *args, **kwargs):
        if not self.id:       
              self.hacker_news_time = datetime.fromtimestamp(int(self.time)) 
        return super(Story, self).save(*args, **kwargs)



"""Comments of Comments are stored as Reply"""

""""
{
  "by": "norvig",
  "id": 2921983,
  "kids": [
    2922097,
    2922429,
    2924562,
    2922709,
    2922573,
    2922140,
    2922141
  ],
  "parent": 2921506,
  "text": "Aw shucks, guys ... you make me blush with your compliments.<p>Tell you what, Ill make a deal: I'll keep writing if you keep reading. K?",
  "time": 1314211127,
  "type": "comment"
}"""

"""
from myapp.models import Genre
rock = Genre.objects.create(name="Rock")
blues = Genre.objects.create(name="Blues")
Genre.objects.create(name="Hard Rock", parent=rock)
Genre.objects.create(name="Pop Rock", parent=rock)
"""

class Comment(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    news = models.ForeignKey(Story, related_name="comments", on_delete=models.CASCADE,blank=True,null=True)
    hn_id = models.CharField(max_length=200,blank=True)
    time = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    hn_parent = models.CharField(max_length=200,blank=True)
    kids = models.CharField(max_length=400,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    hacker_news_time = models.DateTimeField()

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def save(self, *args, **kwargs):
        if not self.id:       
              self.hacker_news_time = datetime.fromtimestamp(int(self.time)) 
        return super(Comment, self).save(*args, **kwargs)