from django.db import models
from django.db.models.deletion import CASCADE


class Group(models.Model):
    groupName = models.CharField(max_length=200)

    def __str__(self):
        return "groupName: " + str(self.groupName)



class Player(models.Model):
    player_name = models.CharField(max_length=100, name="player_name")
    player_telefone_number = models.DecimalField(
        max_digits=12, name="player_telefone_number", decimal_places=0)
    player_group = models.ForeignKey(Group, on_delete=CASCADE)

    def __str__(self):
        return "player_name: " + self.player_name




