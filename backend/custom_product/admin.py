from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from oscar.apps.catalogue.models import Category
from oscar.apps.catalogue.admin import CategoryAdmin as OscarCategoryAdmin  # Import the default admin class

# Unregister the default CategoryAdmin
admin.site.unregister(Category)

# Register your custom CategoryAdmin
@admin.register(Category)
class CategoryAdmin(OscarCategoryAdmin, ImportExportModelAdmin):  # Inherit from Oscar's default CategoryAdmin
    prepopulated_fields = {'slug': ('name',)}  # Add your customizations here

    # Add other customizations as needed
    list_display = ('name', 'slug', 'depth', 'numchild')
    list_filter = ('depth',)
    search_fields = ('name', 'slug')