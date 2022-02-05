from django.db import models
from django.urls import reverse

# Create your models here.
class Nft(models.Model):
    token = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    blockchain = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, default = ' ')

    def __str__(self):
        return self.token

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'nft_id': self.id})
