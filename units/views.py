from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.db.models import Value, IntegerField
from .models import Unit, Race, Worker
from django.db.models import Q
# from django.utils.text import pluralize
from django.template.defaultfilters import pluralize


class UnitsByRaceView(ListView):
    model = Unit
    template_name = 'race_units.html'
    context_object_name = 'units'

    def get_queryset(self):
        race_slug = self.kwargs['race']
        race = get_object_or_404(Race, name__iexact=race_slug)
        return Unit.objects.filter(race=race).annotate(defence_value=Value(0, IntegerField()))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['race'] = get_object_or_404(Race, name__iexact=self.kwargs['race'])
        return context


class AllUnitsByRaceView(ListView):
    model = Unit
    template_name = 'race_units.html'
    context_object_name = 'units'

    def get_queryset(self):
        race_slug = self.kwargs['race']
        race = get_object_or_404(Race, name__iexact=race_slug)
        return Unit.objects.filter(Q(race=race) | Q(worker__race=race)).annotate(defence_value=Value(0, IntegerField())).order_by('name') #showing value of defence even if its 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        race = get_object_or_404(Race, name__iexact=self.kwargs['race'])
        context['race'] = race
        context['race_plural'] = f"{race}{pluralize(race)}"
        return context