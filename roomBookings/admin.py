from django.contrib import admin

# Register your models here.
from roomBookings.models import TimeSlot, Room


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('time_from', 'time_to', 'room_id', 'booked', 'bookedBy')


admin.site.register(Room)
admin.site.register(TimeSlot, TimeSlotAdmin)
