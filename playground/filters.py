import django_filters
from .models import Autists

class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = Autists
        fields= {'name':['exact']}
