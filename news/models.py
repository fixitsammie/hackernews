from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
from datetime import datetime


class Story(models.Model):
    # TODO set updated field as auto_now_add
    created = models.DateTimeField()
    updated = models.DateTimeField()
    score = models.IntegerField()
    hacker_news_item = models.BooleanField()
    creator = models.CharField(max_length=1000)
    hn_id = models.CharField(max_length=200)
    url = models.CharField(max_length=2000)
    type = models.CharField(max_length=200)
    time = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = datetime.utcnow()
        return super(Story, self).save(*args, **kwargs)


class Comm(models.Model):
    hn_id = models.CharField()
    name = models.CharField()
    news = models.ForeignKey(Story, related_name="children", on_delete=models.CASCADE)


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
class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name="replies", on_delete=models.CASCADE)
    created = models. CharField(max_length=200)
    hn_id = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    hn_parent = models.CharField(max_length=200
                                 )
    kids = models.CharField(max_length=400)


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
    created = models.CharField(max_length=200)
    hn_id = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    hn_parent = models.CharField(max_length=200)
    kids = models.CharField(max_length=400)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class MPTTMeta:
        order_insertion_by = ['name']