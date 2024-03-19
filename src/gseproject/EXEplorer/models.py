from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Player(models.Model):
    username = models.CharField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = "User", related_name = "players")
    playerID = models.AutoField(primary_key = True, verbose_name = "Player ID")
    cherry = models.PositiveIntegerField(default = 0, verbose_name = "cherry")
    def __str__(self):
        return f"{self.username} - Player {self.playerID}"


class Tools(models.Model):
    toolsID = models.AutoField(primary_key=True, verbose_name = "Tools ID")
    toolsName = models.CharField(max_length=100, verbose_name = "Tools Name")
    toolsDescription = models.TextField(verbose_name = "Tools Description")

    def __str__(self):
        return self.toolsName

class Tree(models.Model):
    player = models.ForeignKey(Player, on_delete = models.CASCADE, verbose_name = "Player", related_name = "trees")
    tree = models.PositiveIntegerField(default = 0, verbose_name = "tree")
    treeComebackTime = models.DateTimeField(verbose_name = "Comeback Time")
    
    def __str__(self):
        return self.tree
    
