from django.contrib import admin

from pages.models import HomeModel, AboutModel, ProductsModel, CategoryModel, ContactModel


@admin.register(HomeModel)
class HomeAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title', 'description']


@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    search_fields = ['description']
    list_display = ['description']


@admin.register(ProductsModel)
class ProductsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title', 'description']


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'number']
    list_display = ['name', 'number']