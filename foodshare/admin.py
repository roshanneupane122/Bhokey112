from django.contrib import admin
from .models import FoodPost

@admin.register(FoodPost)
class FoodPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'quantity', 'picked_up')
    search_fields = ('name', 'category', 'user__username')
    list_filter = ('category', 'picked_up')

