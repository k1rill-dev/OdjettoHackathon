from django.contrib import admin
from .models import *

# class ExponentAdmin(admin.ModelAdmin):
#     pass
#
#
# class PublicationAdmin(admin.ModelAdmin):
#     pass
#
#
# class CatalogAdmin(admin.ModelAdmin):
#     pass
#
#
# class LocationAdmin(admin.ModelAdmin):
#     pass
#
#
# class PartnerAdmin(admin.ModelAdmin):
#     pass
#
#
# class ReviewAdmin(admin.ModelAdmin):
#     pass
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     pass
#
#
# class ProductAdmin(admin.ModelAdmin):
#     pass
#
#
# class CaseAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Exponent, ExponentAdmin)
# admin.site.register(Publication, PublicationAdmin)
# admin.site.register(Partner, PartnerAdmin)
# admin.site.register(Review, ReviewAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Case, CaseAdmin)

admin.site.register(Exponent)
admin.site.register(Publication)
admin.site.register(Partner)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Case)
admin.site.register(User)
