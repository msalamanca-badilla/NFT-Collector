from django.contrib import admin
from .models import Nft, Selling
# Register your models here.
from .models import Nft
admin.site.register(Nft)
admin.site.register(Selling)
