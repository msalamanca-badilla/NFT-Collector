from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Nft
from .forms import SellingForm
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
  selling_form=SellingForm()
  return render(request, 'nfts/detail.html', { 
    'nft': nft,'selling_form': selling_form
     })

class NftCreate(CreateView):
  model = Nft
  fields = '__all__'

class NftUpdate(UpdateView):
  model = Nft
  fields = ['owner']

class NftDelete(DeleteView):
  model=Nft
  success_url='/nfts'

def add_selling(request, nft_id):
  # create a ModelForm instance using the data in request.POST
  form = SellingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_selling = form.save(commit=False)
    new_selling.nft_id = nft_id
    new_selling.save()
  return redirect('detail', nft_id=nft_id)