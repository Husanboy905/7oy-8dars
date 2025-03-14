from django.contrib import admin
from .models import Category, Product, Image, Comment
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')  # 'parent' ni olib tashlang
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'image')
#     prepopulated_fields = {'slug': ('name',)}
#     inlines = [ImageInline]

# # admin.site.register(Product, ProductAdmin)
# admin.site.register(Comment)
# from django.contrib import admin
# from .models import  Product, Image
#
# admin.site.register(Product)
# admin.site.register(Image)
