from django.contrib import admin

from .models import *

# Register your models here.


# admin.site.register(User)
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display=['name','email','roles','gender','address']

@admin.register(Slot)
class AdminSlot(admin.ModelAdmin):
    list_display=['id','doctor_id','timeslot','weeks']