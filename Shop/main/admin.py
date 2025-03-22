from django.contrib import admin
from .models import Category, Product, Image, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount', 'final_price')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Image)
admin.site.register(Comment)


from django.contrib import admin
from .models import Order, OrderProduct, City, Delivery

admin.site.register(City)
admin.site.register(Delivery)

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at')
    inlines = [OrderProductInline]
