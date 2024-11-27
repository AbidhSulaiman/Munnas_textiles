from django.contrib import admin
from .models import Category, Tag, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of empty image forms to show
    fields = ('image', 'alt_text', 'order')
    ordering = ('order',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'category', 'price', 'discount', 'stock', 'is_available', 'created_at', 'updated_at')
    list_filter = ('category', 'tags', 'is_available', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    filter_horizontal = ('tags',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'description','available_size', 'price', 'discount', 'stock', 'is_available', 'tags')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

