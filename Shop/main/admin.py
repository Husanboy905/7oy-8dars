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
    list_display = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Image)
admin.site.register(Comment)
