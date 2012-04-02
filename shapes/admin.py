from django.contrib import admin
from models import Item, Shape

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ShapeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Item, ItemAdmin)
admin.site.register(Shape, ShapeAdmin)
