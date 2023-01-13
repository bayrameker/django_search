from django.contrib import admin

# Register your models here.

from app.models import Price, Coin


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    fields = ('currency', 'coin', 'price', 'transactionAt',)
    list_display = ('id', 'currency', 'coin', 'price', 'transactionAt',)
    search_fields = ('currency', )
    list_per_page = 5


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    fields = ('name',)
    list_per_page = 5
