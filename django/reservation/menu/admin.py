from django.contrib import admin
from .models import Booking
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    #list_display = ("date","time","user_name","user_email","approved","user_mobile","created_at","status")
    list_display = [field.name for field in Booking._meta.get_fields()]
    list_filter = ("approved", "date")
    ##list_editable = ('created_at')
    list_display_links = ('user_name', 'approved')
    ordering = ("date", "time")
    search_fields = ["user_name"]
    list_per_page = 25

admin.site.register(Booking,BookingAdmin)