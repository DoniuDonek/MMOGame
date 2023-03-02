from django.test import TestCase
from django.contrib.auth.models import User
from .models import Mineral, Gas, Population

class ResourceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.mineral = Mineral.objects.create(
            user=self.user,
            current_amount=50,
        )
        self.gas = Gas.objects.create(
            user=self.user,
            current_amount=0,
        )
        self.population = Population.objects.create(
            user=self.user,
            starting_amount=9,
            max_population=200,
        )

    def test_mineral_model(self):
        self.assertEqual(str(self.mineral), "testuser's Minerals")
        self.assertEqual(self.mineral.user, self.user)
        self.assertEqual(self.mineral.current_amount, 50)

    def test_gas_model(self):
        self.assertEqual(str(self.gas), "testuser's Gas")
        self.assertEqual(self.gas.user, self.user)
        self.assertEqual(self.gas.current_amount, 0)

    def test_population_model(self):
        self.assertEqual(str(self.population), "testuser's Population")
        self.assertEqual(self.population.user, self.user)
        self.assertEqual(self.population.starting_amount, 9)
        self.assertEqual(self.population.max_population, 200)