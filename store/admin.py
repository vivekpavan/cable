from django.contrib import admin
from django.utils.html import format_html,urlencode
from django.urls import reverse
from . import models
from django.db.models import Count,Sum

# Register your models here.
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =  ['name','payment_status_counter','last_payment_date','channel_title','channel_count','total_price']
    list_per_page = 10
    
    @admin.display(ordering = 'payment_status')
    def payment_status_counter(self,customer):
        if customer.payment_status == True:
            return 'done'
        return 'not done'

    def channel_title(self,customer):
        return ' - '.join([ch.channel_name for ch in customer.channels_set.all()])

    @admin.display(ordering = 'channel_count')
    def channel_count(self,customer):
        url = (
            reverse('admin:store_channels_changelist')
            + '?'
            + urlencode({
                'customer__id': str(customer.id)
            }))
        return format_html('<a href="{}">{}</a>',url,customer.channel_count)
        
    
    def total_price(self,customer):
        return customer.total_price
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('channels_set').annotate(
            channel_count = Count('channels'),
            total_price = Sum('channels__channel_price')
        )
    
@admin.register(models.Channels)
class ChannelAdmin(admin.ModelAdmin):
    models.Channels.objects.all().select_related('customer')
    list_display = ['channel_name','channel_price','customer_name','customer_count']
    ordering = ['id']
    list_per_page =  10

    def customer_name(self,channels):
        return " , ".join([c.name for c in channels.customer.all()])

    @admin.display(ordering = 'customer_count')
    def customer_count(self,channels):
        return channels.customer_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('customer').annotate(
            customer_count = Count('customer')
        )

@admin.register(models.Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = ['box_no','customer']
    list_select_related = ['customer']