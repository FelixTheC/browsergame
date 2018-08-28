from django.contrib.auth.models import User
from django.db import models
from spell.models import Spell


class Player(User):
    class Meta:
        ordering = 'pk'
        db_table = 'player'

    level = models.IntegerField(default=0, blank=True)
    xp = models.DecimalField(default=0.0, blank=True)
    live_points = models.PositiveIntegerField(default=100, blank=True)
    max_live_points = models.PositiveIntegerField(default=100, blank=True)
    mana_points = models.PositiveIntegerField(default=50, blank=True)
    max_mana_points = models.PositiveIntegerField(default=50, blank=True)
    armor_points = models.DecimalField(default=5.0, blank=True)
    spells = models.ManyToManyField(Spell)

    def __str__(self):
        return self.username

    def __repr__(self):
        return f'Player - {self.pk}'