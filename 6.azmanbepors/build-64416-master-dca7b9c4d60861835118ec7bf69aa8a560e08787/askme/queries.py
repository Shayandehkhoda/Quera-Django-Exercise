from askme.models import Brand, Mobile
from django.db.models import *

def total_value_of_products():
    query = Mobile.objects.aggregate(total_value=Sum('price'))
    return query


def total_value_of_products_with_brand_of(brand_name):
    query = Mobile.objects.filter(brand__name=brand_name).aggregate(total_value=Sum('price'))
    return query


def most_expensive_cheapest_price_with_nationality_of(nationality):
    query = Mobile.objects.filter(brand__nationality=nationality).aggregate(cheap=min('price'), expensive=max('price'))
    return query


def display_size_avg_in_available_mobiles_between_price(minimum, maximum):
    query = Mobile.objects.filter(is_available=True).filter(price__lte=maximum).filter(price__gte=minimum).aggregate(avg=Avg('display_size'))
    return query

