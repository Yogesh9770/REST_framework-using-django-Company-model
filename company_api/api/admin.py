from django.contrib import admin
from api.models import Company, Employee
# Register your models here.

class  CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_location','company_types')
    search_fields = ('company_name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_first_name','employee_last_name','company')
    list_filter = ( 'company',)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)   
