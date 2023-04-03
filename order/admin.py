from django.contrib import admin

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

admin.site.register(Order, OrderAdmin)