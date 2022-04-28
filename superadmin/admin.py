from django.contrib import admin

from superadmin.models import User

# Register your models here.


# admin.site.register(User)
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display=['name','email','roles','gender','address']