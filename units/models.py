from django.db import models
from django.utils.text import slugify


class Race(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Race, self).save(*args, **kwargs)


    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=50)
    race = models.ForeignKey(Race, on_delete=models.CASCADE,  default=None)
    attack = models.PositiveIntegerField(blank = False, default = 5)
    defence = models.PositiveIntegerField(blank = False, default = 0)
    speed = models.PositiveIntegerField(blank = False, default = 10)
    health = models.PositiveIntegerField(blank = False, default = 50)
    description = models.TextField(max_length=1000)
    photo = models.ImageField(blank=False)
    mineral_cost = models.PositiveIntegerField(blank = False, default = 0)
    gas_cost = models.PositiveIntegerField(blank = False, default = 0)
    capacity = models.PositiveIntegerField(blank = False, default = 1)
    anti_air = models.BooleanField(blank = False, default =False)
    flying_unit = models.BooleanField(blank = False, default = False)

    def range_attack(self):
        pass

    def __str__(self):
        return self.name


class Worker(Unit):
    unit_ptr = models.OneToOneField(Unit, parent_link=True, related_name='worker', primary_key=True, on_delete=models.CASCADE, default=None)
    collected_minerals = models.PositiveIntegerField(default=0)
    
    def range_attack(self):
        pass

    def __str__(self):
        return self.name
    