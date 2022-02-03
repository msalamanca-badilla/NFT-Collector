from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('nfts/',views.nfts_index,name='index'),
    path('nfts/<int:nft_id>/', views.nfts_detail,name='detail')
]