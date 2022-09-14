from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_barang': data_katalog_item,
        'nama': 'Febi Claudia Damanik',
        'NPM' : '2106751884'
    }
    return render(request, "katalog.html", context)