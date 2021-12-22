from django.contrib import admin

# Register your models here.
from reservation.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'car', 'total', 'status', 'rezdate', 'returndate', 'create_at']
    list_filter = ['status']
    readonly_fields = ('last_name','country', 'address', 'city', 'phone', 'first_name', 'total')


admin.site.register(Reservation, ReservationAdmin)
