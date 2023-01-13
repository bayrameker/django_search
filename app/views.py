from django.views.generic import TemplateView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, LazyPaginator

from app.filter import CoinFilter
from app.models import Price, Coin
from app.table import CoinTable


class PriceChartView(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Price.objects.all()
        return context


class HomeListView(SingleTableMixin, FilterView):
    table_class = CoinTable
    queryset = Coin.objects.all()
    template_name = "home.html"
    filterset_class = CoinFilter
    paginate_by = 2
    paginator_class = LazyPaginator
