from django.contrib import admin

from .models import *

# Register your models here.


# admin.site.register(User)
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display=['id','name','email','roles','gender','address']

@admin.register(Slot)
class AdminSlot(admin.ModelAdmin):
    list_display=['id','doctor_id','doc_name','timeslot','weeks']
    def doc_name(self, obj):
        return obj.doctor_id.name

@admin.register(Appoinment)
class AdminAppoinment(admin.ModelAdmin):
    list_display =['id','doc_name','slot','patient_name','status']
    def doc_name(self, obj):
        return obj.slot.doctor_id.name