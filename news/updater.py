from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .updateNews import update_news


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_news, 'interval', minutes=5)
    #job1.remove()
    #scheduler.remove()
    scheduler.start()

#TODO change minutes back to 5