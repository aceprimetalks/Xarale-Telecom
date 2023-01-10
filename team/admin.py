from django.contrib import admin
from .models import Staff, Staff_Social


admin.site.register(Staff)
admin.site.register(Staff_Social)

list_display = ('id', 'trip_number', 'trip_link')




def trip_link(self, obj):
        if obj.trip_number:
            return "<a href='%s'>Link</a>" % obj.trip_number
        else:
            return ''