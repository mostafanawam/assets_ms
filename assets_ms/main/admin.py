from django.contrib import admin
from .models import Asset, Employee, Lending

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status')  # Customize what fields are shown in the admin list
    list_filter = ('status', 'category')  # Add filters for status and category
    search_fields = ('name', 'category')  # Add search functionality for name and category
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Customize what fields are shown in the admin list
    search_fields = ('name',)  # Add search functionality for name and category





@admin.register(Lending)
class LendingAdmin(admin.ModelAdmin):
    list_display = ('asset', 'employee', 'lend_date',  'return_date',)
    list_filter = ('asset', 'employee', 'lend_date')  # Add filters for asset, employee, and lending date
    search_fields = ('asset__name', 'employee__user__username')  # Search by asset name or employee username
    date_hierarchy = 'lend_date'  # Add a date hierarchy for lend date

    # Make is_overdue method available in the admin list
    # def is_overdue(self, obj):
    #     return obj.is_overdue()
    # is_overdue.boolean = True  # Show as a boolean icon in the admin list
    # is_overdue.short_description = 'Overdue?'  # Label for the boolean column
