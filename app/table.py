import django_tables2 as tables

from app.models import Coin


class CoinTable(tables.Table):
    class Meta:
        model = Coin
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )

