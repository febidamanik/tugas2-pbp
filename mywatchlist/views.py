from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    mywatchlist = MyWatchList.objects.all()
    
    watched = MyWatchList.objects.filter(watched=True).count()
    unwatched = MyWatchList.objects.filter(watched=False).count()

    message = ""

    # menampilkan pesan 
    if watched >= unwatched:
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        "watchlist": mywatchlist,
        "message": message,
        "nama": 'Febi Claudia Damanik',
        "npm": "2106751884"
    }
    return render(request, 'mywatchlist.html', context)

def show_mywatchlist_json(request):
    mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", mywatchlist), content_type="application/json")

def show_mywatchlist_xml(request):
    mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", mywatchlist), content_type="application/xml")