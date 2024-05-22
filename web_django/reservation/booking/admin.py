from django.contrib import admin

# Register your models here.
from booking.models import Booking, BookingSettings


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    #list_display = ("user_email", "user_name", "date", "time", "approved")
    list_display = [field.name for field in Booking._meta.get_fields()]
    list_filter = ("approved", "date")
    ordering = ("date", "time")
    search_fields = ("user_email", "user_name")

admin.site.register(BookingSettings)