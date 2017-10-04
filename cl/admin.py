from django.contrib import admin
from .models import ContingentLeader


class ContingentLeaderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_mi_number', 'get_college')
    list_filter = ['clprofile__present_college__college_name']
    readonly_fields = ('get_mi_number', 'get_college',)


# Register your models here.
admin.site.register(ContingentLeader, ContingentLeaderAdmin)
