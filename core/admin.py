from django.contrib import admin

from .models import Customer , EmailTemplate

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'dob', 'consent')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('dob',)
@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ("subject", "active")

# Register your models here.
