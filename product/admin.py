from django.contrib import admin

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Product, ProductAdmin)