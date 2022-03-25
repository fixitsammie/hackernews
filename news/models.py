from django.db import models
from datetime import datetime


class Story(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    score = models.IntegerField(blank=True)
    hacker_news_item = models.BooleanField()
    creator = models.CharField(max_length=1000)
    text = models.CharField(max_length=2000)
    hn_id = models.CharField(max_length=200,blank=True)
    url = models.CharField(max_length=2000)
    type = models.CharField(max_length=200,blank=True)
    time = models.CharField(max_length=200,blank=True)
    hacker_news_time = models.DateTimeField()
    title =models.CharField(max_length=1000,blank=True)

    def __str__(self):
          return self.text
    
 

    

    def save(self, *args, **kwargs):
        if not self.id and self.time:       
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



class Comment(models.Model):
    name = models.CharField(max_length=50, unique=True)
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
    parent_comment = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='reply')

   
    
    def __str__(self):
          return self.text
          
    def save(self, *args, **kwargs):
        if not self.id:       
              self.hacker_news_time = datetime.fromtimestamp(int(self.time)) 
        return super(Comment, self).save(*args, **kwargs)