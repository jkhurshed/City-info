from django.contrib import admin
from django.contrib.auth.models import Group
from cityApp.models import Category, City, Place, Contact

admin.site.unregister(Group)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):

    model = Place
    list_display = ("id", "title", "description", "category", "adress", "city")
    list_filter = ("title",)
    search_fields = ("title", "city")
    list_display_links = ("title",)
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
