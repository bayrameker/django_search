import django_filters

from app.models import Coin


class CoinFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(
        method='universal_search',
        label="",
    )

    class Meta:
        model = Coin
        fields = ['query']

    def universal_search(self, queryset, name, value):
        return Coin.objects.filter(name__contains=value)
