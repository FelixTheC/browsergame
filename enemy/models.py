from django.db import models
from element.models import Element


class Enemy(models.Model):
    class Meta:
        db_table = 'enemy'

    name = models.CharField(max_length=255)
    level = models.PositiveIntegerField()
    live_points = models.DecimalField()
    resist_against_element = models.ForeignKey(Element, on_delete=models.SET_NULL)
    weak_against_element = models.ForeignKey(Element, on_delete=models.SET_NULL)
    max_hit_points = models.DecimalField()
    min_hit_points = models.DecimalField()
    armor_points = models.DecimalField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Enemy - {self.pk}'