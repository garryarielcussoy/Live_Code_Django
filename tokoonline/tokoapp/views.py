from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Barang, Deskripsi
# from .models import Blog, Mentee, Mentor

# Create your views here.
def index(request):
    barangs = Barang.objects.all()
    return render(request, 'tokoapp/index.html', {'barangs': barangs})

def detail_barang(request, barang_id):
    deskripsi = Deskripsi.objects.filter(id_barang = barang_id)
    barang = Barang.objects.get(pk = barang_id)
    sent = {
        'deskripsi' : deskripsi,
        'barang' : barang
    }
    return render(request, 'tokoapp/detail_barang.html', sent)