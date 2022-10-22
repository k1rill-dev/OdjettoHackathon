from django.contrib import admin
from .models import *


class ExponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'inn_exponent', 'moderation_passed',)
    list_display_links = ('moderation_passed',)
    search_fields = ('name', 'id', 'category',)
    list_editable = ('inn_exponent',)
    list_filter = ('moderation_passed',)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'moderation_passed',)
    list_display_links = ('moderation_passed',)
    search_fields = ('name', 'id',)
    # list_editable = ('moderation_passed',)
    list_filter = ('moderation_passed', 'date_of_create',)


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('category', 'publish_price',)
    list_display_links = ('category',)
    search_fields = ('category', 'id',)
    list_editable = ('publish_price',)
    list_filter = ('category',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'gps_coordination', 'name', 'moderation_passed',)
    list_display_links = ('moderation_passed',)
    search_fields = ('address', 'id',)
    list_editable = ('address',)
    list_filter = ('moderation_passed', 'exponent',)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'exponent', 'display_order', 'is_published',)
    list_display_links = ('is_published',)
    search_fields = ('name', 'id',)
    # list_editable = ('is_published',)
    list_filter = ('is_published', 'exponent',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('grade', 'author', 'moderation_passed', 'is_published',)
    list_display_links = ('moderation_passed',)
    search_fields = ('author', 'id',)
    # list_editable = ('is_published', 'moderation_passed')
    list_filter = ('is_published', 'date_of_create',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'moderation_passed', 'is_published',)
    list_display_links = ('moderation_passed',)
    search_fields = ('name', 'id',)
    # list_editable = ('is_published',)
    list_filter = ('is_published', 'date_of_create',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'brand', 'name', 'price', 'is_published', 'moderation_passed',)
    list_display_links = ('moderation_passed',)
    search_fields = ('name', 'id',)
    # list_editable = ('is_published', 'moderation_passed')
    list_filter = ('is_published', 'moderation_passed',)


class CaseAdmin(admin.ModelAdmin):
    list_display = ('url', 'exponent', 'name', 'is_published', 'moderation_passed',)
    list_display_links = ('moderation_passed',)
    search_fields = ('name', 'id',)
    # list_editable = ('is_published',)
    list_filter = ('is_published', 'moderation_passed',)


admin.site.register(Exponent, ExponentAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(User)
admin.site.register(Catalog, CatalogAdmin)
