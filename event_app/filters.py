import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    location = django_filters.CharFilter(field_name="location", lookup_expr='icontains')
    status = django_filters.ChoiceFilter(field_name='status', choices=Event.StatusChoices.choices)
    category = django_filters.ModelChoiceFilter(queryset=Event.objects.values_list('category', flat=True).distinct())

    class Meta:
        model = Event
        fields = ['title', 'location', 'status', 'category']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.filters.items():
            field.field.widget.attrs.update({
                'class': 'form-control',   # Bootstrap form styling
                'placeholder': f'Search {field_name.capitalize()}'
            })