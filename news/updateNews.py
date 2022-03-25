"""
Retrieve news from the api
"""
from .models import Story,Comment
import requests
import datetime

max_count = 100
count = 0
""""

{
"by": "bnr",
"descendants": 119,
"id": 30503482,
"kids": [
30505328,
30504550,
30504929,
30504516,
30504846,
30512008,
30509870,
30506110,
30504056,
30504667,
30505460,
30504686,
30508040,
30505160,
30504079,
30504507,
30508454,
30504561,
30507303,
30505198,
30504436
],
"score": 366,
"time": 1646074319,
"title": "No user accounts, by design",
"type": "story",
"url": "https://f-droid.org/en/2022/02/28/no-user-accounts-by-design.html"
}

"""

#500 top stories and news
top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
#200 top news
top_news_stories = "https://hacker-news.firebaseio.com/v0/showstories.json?print=pretty"
def _get_news_json():
    url = top_stories_url
    r = requests.get(url)

    try:
        r.raise_for_status()
        return r.json()
    except:
        return None


def get_news(news_id):
    url = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(news_id)
    r = requests.get(url)
    try:
        r.raise_for_status()
        return r.json()
    except:
        return None


def get_kid(kid_id):
    url = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(kid_id)
    r = requests.get(url)
    try:
        r.raise_for_status()
        return r.json()
    except:
        return None


def save_replies(replies, parent_comment):
    for reply in replies:
        reply_object = get_kid(reply)
        if reply_object and not Comment.objects.filter(hn_id = reply_object['id']).exists():
            comment = Comment(
                text = reply_object['text'],
                hn_id = reply_object[id],
                parent_comment = parent_comment
            ).save()
            if reply_object and reply_object['kids']:
                save_replies(reply_object['kids'],comment)



def update_kids(kids,parent_object):
    for kid in kids:
        kid_object = get_kid(kid)
        if kid_object:
            parent_object = save_comment(kid_object, parent_object)
        if kid_object and kid_object['kids'] and parent_object:
            save_replies(replies = kid_object['kids'], parent_comment = parent_object)



def save_comment(kid,parent):
    """parent is an instance of Story model, kid is a json object"""
    if not Comment.objects.filter(hn_id = kid['id']).exists():
        comment = Comment(
            text =kid['text'],
            hn_id = kid['id'],
            parent=parent
        )
        comment.save()
        print("Comment saved")
        return comment
    return None


def single_news(news_id):
    json = get_news(news_id)
    if json is not None:
        if not Story.objects.filter(hn_id=json['id']).exists():
            try:
                new_story = Story(
                    created =   datetime.datetime.now() ,
                score=   json['score'] ,
                hacker_news_item= True    ,
                creator =  json['by']  ,
                hn_id =  json['id']  ,
                title =   json['title'] ,
                url =  json['url']  ,
                type =  json['type']  ,
                time =   json['time'] ,

                )
                new_story.save()

                print("New story saved: {}".format(json['title']))
                count = count +1
                if new_story:
                    update_kids(json['kids'],new_story)

                new_story.created = datetime.datetime.now()
                new_story.score = json['time']
                new_story.hn_id = json['id']
                #TODO convert time to timestamp object
                new_story.save()
            except:
                pass

def update_news():
    global max_count
    global count
    story_count = Story.objects.all().count()
    if story_count == 0:
        max_count = 250
    else:
        max_count = 100
    news_list = _get_news_json()
    for i in news_list:
        if (count<=max_count):
            single_news(i)
    