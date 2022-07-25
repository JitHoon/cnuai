from pyexpat import model
from django.db import models

# Create your models here.


class CpuTeam(models.Model):
    # field1 = models.Field()
    def __str__(self):
        return self.name

    name = models.CharField(default="", null=False, max_length=10)
    studentID = models.IntegerField(default=0)
    cool = models.BooleanField(default=False)
