from django.contrib import admin
from employee_information.models import Department, Position, Employees, CostomUser, Arizalar, Muddat
from django.contrib.auth.admin import UserAdmin
from .forms import RegisterForm
# Register your models here.
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(Arizalar)
admin.site.register(Muddat)

class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    model = CostomUser
    list_display = ['email','username','first_name','last_name','is_admin', 'is_operator', 'is_shop','is_shop_child','parent','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_admin', 'is_operator', 'is_shop','is_shop_child','parent')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('is_admin', 'is_operator', 'is_shop','is_shop_child','parent')}),
    )

admin.site.register(CostomUser, CustomUserAdmin)