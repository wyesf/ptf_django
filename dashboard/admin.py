from django.contrib import admin
from .models import Opexseoul

# Register your models here.
class DashboardAdmin(admin.ModelAdmin) :
    list_display = ('regDate','restaurant','personnel','price','borough')

admin.site.register(Opexseoul, DashboardAdmin)