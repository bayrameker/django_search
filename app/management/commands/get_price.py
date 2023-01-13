import logging
from datetime import datetime

import requests
from django.core.management import BaseCommand

from app.models import Coin, Price

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("commands: price ")

        response = requests.get("https://api.coinstats.app/public/v1/charts?period=1m&coinId=bitcoin")
        json = response.json()
        chart_list = json["chart"]
        price_list = []
        c, _ = Coin.objects.update_or_create(
            name="USD"
        )
        for chart in chart_list:
            price_list.append(
                Price(
                    transactionAt=datetime.fromtimestamp(chart[0]),
                    price=chart[1],
                    coin_id=c.id,
                )
            )
        Price.objects.bulk_create(price_list)
