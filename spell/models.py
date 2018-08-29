from django.db import models
from element.models import Element


class Spell(models.Model):
    class Meta:
        db_table = 'spell'
    name = models.CharField(max_length=255)
    mana_cost = models.DecimalField()
    element_type = models.ForeignKey(Element, on_delete=models.SET_NULL)
    max_hit_points = models.DecimalField()
    min_hit_points = models.DecimalField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Spell - {self.pk}'