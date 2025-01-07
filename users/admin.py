from django.contrib import admin
from .models import Profile,CustomUser

class ProfileAdmin(admin.ModelAdmin):
    list_display =['user','bio','birth_date','avatar']

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone_number']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
