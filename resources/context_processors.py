from resources.models import Mineral, Gas, Population

def resources(request):
    minerals = None
    gas = None
    population = None
    if request.user.is_authenticated:
        minerals = Mineral.objects.get_or_create(user=request.user)[0].current_amount
        gas = Gas.objects.get_or_create(user=request.user)[0].current_amount
        population = Population.objects.get_or_create(user=request.user)[0]

    return {
        'minerals': minerals,
        'gas': gas,
        'population': population,
    }