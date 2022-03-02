from django.db import models

# Create your models here.
from datetime import datetime

class Story(models.Model):
    #TODO set updated field as auto_now_add
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


class Comment(models.Model):
    hn_id = models.CharField()
    name = models.CharField()
    news = models.ForeignKey(Story,related_name="children", on_delete=models.CASCADE)