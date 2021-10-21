from django.db import models
from django.db.models.deletion import CASCADE


class Group(models.Model):
    group_number = models.DecimalField(
        decimal_places=0, max_digits=2, name="group_number")

    def __str__(self):
        return "group_number: " + str(self.group_number)



class Player(models.Model):
    player_name = models.CharField(max_length=100, name="player_name")
    player_telefone_number = models.DecimalField(
        max_digits=12, name="player_telefone_number", decimal_places=0)
    player_group = models.ForeignKey(Group, on_delete=CASCADE)

    def __str__(self):
        return "player_name: " + self.player_name




