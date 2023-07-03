# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from urunApp.models import *
from urunApp.form import GetReservation

# Randevu Sayfasi
def randevu(request):
    

    return render(request, 'randevu.html')



def makeRandevu(request, randevuId):
    print("ID:", randevuId)
    if request.method == 'POST':
        randevuId = int(randevuId)        

        rezervasyonItem = Reservation.objects.filter(id=randevuId).first()
        tel = request.POST.get('tel')
        MakeAppointment.objects.create(user=request.user, rezervasyon=rezervasyonItem, tel=tel ).save()
        return redirect('randevu')
    
    else:
          return redirect('anasayfa')


# user kayit olursa
@login_required(login_url='user-login')
def reservation(request):
    context = {}
    randevuForm = GetReservation()
    if request.method == 'POST':
      pass

    else:
        context['form'] = randevuForm
        reservations = Reservation.objects.all()
        context["reservations"] = reservations

        return render(request, 'randevu.html', context)