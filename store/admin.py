from typing import Any
from django.contrib import admin,messages
from django.urls import reverse
from django.db.models.query import QuerySet
from django.db.models import Count
from django.http import HttpRequest
from django.utils.html import format_html,urlencode
from . import models
# Register your models here.
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    search_fields = ['title']

    def products_count(self,collection):
        url = (
            reverse('admin:store_product_changelist') 
            + '?'
            + urlencode({
                'collection__id':str(collection.id)
            })
        )
        return format_html('<a href="{}">{}</a>',url,collection.products_count)
        
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'LOW')
        ]

    def queryset(self, request, queryset: QuerySet[Any]):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=50)



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    autocomplete_fields = ['collection']
    list_display = ['title','unit_price','inventory_status','collection_set']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    list_filter = ['collection','last_update',InventoryFilter]
    prepopulated_fields = {
        'slug': ['title']
    }
    search_fields = ['title']

    def collection_set(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 50:
            return 'LOW'
        return 'OK'
    
    @admin.action(description='Clear Inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory = 0)
        self.message_user(
            request,
            f"{updated_count} products were successfully updated",
            messages.ERROR
        )


# admin.site.register(models.Product, ProductAdmin)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','membership','orders_count']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name','last_name']
    search_fields = ['first_name__istartswith','last_name__istartswith']
    

    @admin.display(ordering='orders_count')
    def orders_count(slf, customer):
        url = (
            reverse("admin:store_order_changelist")
            + '?'
            + urlencode({
                'customer__id':customer.id
            })
        )
        return format_html('<a href = "{}">{}</a>', url, customer.orders_count)
        
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count = Count('order')
        )

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    autocomplete_fields = ['product']

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','customer']
    inlines = [OrderItemInline]


