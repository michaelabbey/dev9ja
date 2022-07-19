from django.contrib import admin
from . models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','phone', 'email', 'message', 'created']
    list_display_links = ['id', 'name','phone']

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'first_name', 'last_name', 'phone', 'age', 'sex', 'i_am_registering_for', 'location', 'does_your_child_have_any_experience_coding', 'created']
    list_display_links = ['id', 'email','phone']


admin.site.register(Contact,ContactAdmin)   
admin.site.register(Registration,RegistrationAdmin)    