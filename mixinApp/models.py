from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=25)
    score = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.id}: {self.name}"
