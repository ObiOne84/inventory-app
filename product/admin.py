from django.contrib import admin
from .models import Category, Product, Subcategory


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sku', 'type', 'color', 'gender',
                    'usage', 'description',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
