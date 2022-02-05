from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Nft
# Define the home view

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
def about(request):
  return render(request, 'about.html')
def nfts_index(request):
  nfts = Nft.objects.all()
  return render(request, 'nfts/index.html', { 'nfts': nfts })
def nfts_detail(request, nft_id):
  nft = Nft.objects.get(id=nft_id)
  return render(request, 'nfts/detail.html', { 'nft': nft })

class NftCreate(CreateView):
  model = Nft
  fields = '__all__'