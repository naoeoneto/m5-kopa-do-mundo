from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.BigIntegerField(default=0, blank=True, null=True)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3)
    first_cup = models.DateField(auto_now=False, blank=True, null=True)

    def __repr__(self):
        return f'<[{id} {Team.name} - {Team.fifa_code}]'
