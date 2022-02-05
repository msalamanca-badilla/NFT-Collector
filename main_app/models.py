from django.db import models

# Create your models here.
class Nft(models.Model):
    token = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    blockchain = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, default = ' ')

    def __str__(self):
        return self.token