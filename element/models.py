from django.db import models


class Element(models.Model):
    class Meta:
        db_table = 'element'
        ordering = 'name'

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Element - {self.pk}'