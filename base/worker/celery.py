import os
import time

from celery import Celery
from apps.reviews.scraper import scrape_google_reviews
from apps.reviews.custom_types import SCRAPED_DATA_TYPE

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379"
)


@celery.task(name="create_task")
def scrape_task():
    return "check done"

