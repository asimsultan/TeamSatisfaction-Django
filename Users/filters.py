# Importing Libraries
from django_filters import FilterSet
from .models import UserHappiness


class UserFilterSet(FilterSet):
    class Meta:
        model = UserHappiness
        fields = ('happiness_level', 'username')
