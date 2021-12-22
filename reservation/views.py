from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
# Create your views here.
from car.models import Car, Category
from home.models import UserProfile
from reservation.models import Reservation, ReservationForm


def index(request):
    rez = Reservation.objects.all()
    category = Category.objects.all()
    car = Car.objects.all()
    context = {
        'rez': rez,
        'category': category,
        'car': car,
    }
    return render(request, 'reservation.html', context)


@login_required(login_url='/login')
def reservationproduct(request, id):
    global reservationcode
    current_user = request.user
    productz = Car.objects.filter(pk=id)
    days = 0
    total = 0

    if request.method == 'POST':  # if there is a post
        form = ReservationForm(request.POST)
        category = Category.objects.all()
        # return HttpResponse(request.POST.items())
        if form.is_valid():
            #
            # ..............

            data = Reservation()
            for rs in productz:
                data.car_id = id

            data.first_name = current_user.first_name
            data.last_name = current_user.last_name
            data.address = current_user.userprofile.address
            data.city = current_user.userprofile.city
            data.phone = current_user.userprofile.phone
            data.rezdate = form.cleaned_data['rezdate']
            data.returndate = form.cleaned_data['returndate']
            delta = data.returndate - data.rezdate
            data.days = delta.days
            for rs in productz:
                total = rs.price * data.days
            data.total = total

            data.user_id = current_user.id

            data.ip = request.META.get('REMOTE_ADDR')
            reservationcode = get_random_string(5).upper()  # random cod
            data.code = reservationcode
            data.save()  #
        else:
            #
            # ..............

            data = Reservation()
            for rs in productz:
                data.car_id = id

            data.first_name = current_user.first_name
            data.last_name = current_user.last_name
            data.address = current_user.userprofile.address
            data.city = current_user.userprofile.city
            data.phone = current_user.userprofile.phone
            data.rezdate = form.cleaned_data['rezdate']
            data.returndate = form.cleaned_data['returndate']
            delta = data.returndate - data.rezdate
            data.days = delta.days
            for rs in productz:
                total = rs.price * data.days
            data.total = total

            data.user_id = current_user.id

            data.ip = request.META.get('REMOTE_ADDR')
            reservationcode = get_random_string(5).upper()  # random cod
            data.code = reservationcode
            data.save()  #

    form = ReservationForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'category': category,
        'productz': productz,
        'reservationcode': reservationcode,
        'form': form,
        'total': total,
        'profile': profile,
    }
    return render(request, 'reservation.html', context)
