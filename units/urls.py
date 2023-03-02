from django.urls import path
from .views import UnitsByRaceView


urlpatterns = [
    path('race/<slug:race>/', UnitsByRaceView.as_view(template_name='race_units.html'), name='race_units'),
]