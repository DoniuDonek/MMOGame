from celery import shared_task
from accounts.models import CustomUser
from resources.models import Mineral, Gas, Population

@shared_task
def collect_resources(user_id):
    user = CustomUser.objects.get(id=user_id)
    minerals = Mineral.objects.get(user=user)
    gas = Gas.objects.get(user=user)
    population = Population.objects.get(user=user)

    # Collect minerals with drones
    minerals_per_drone_per_cycle = 8
    minerals_per_cycle = minerals_per_drone_per_cycle * population.drones
    minerals.amount += minerals_per_cycle

    # Save the updated models
    minerals.save()
    gas.save()
    population.save()