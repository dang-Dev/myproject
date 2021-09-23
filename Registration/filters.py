import django_filters
from django_filters import DateFilter, DateTimeFromToRangeFilter
from .models import *


class logbookFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_time_in", lookup_expr='gte',)
    end_date = DateFilter(field_name="date_time_in", lookup_expr='lte')
    class Meta:
        model = Logbook
        exclude = ('id_number','first_name', 'last_name', 'middle_name', 'age', 'gender', 'address', 'course', 'block', 'year', 'body_temp', 'cp_number', 'date_time_in', 'date_time_exit')
        fields = '__all__'
 