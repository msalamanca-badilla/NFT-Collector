from xmlrpc.client import boolean
from django.db import models
from django.urls import reverse

SELL = (
    ('S', 'Selling'),
    ('S', 'Sold')
)

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

class Selling(models.Model):
    date = models.DateField('Selling Date')
    sell = models.CharField(
        max_length=1,
        choices=SELL,
        default=SELL[0][0]
    )

    nft = models.ForeignKey(Nft, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_sell_display()} on {self.date}"