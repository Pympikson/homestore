from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import Listing


class ListingResource(resources.ModelResource):
  class Meta:
    model = Listing
    fields = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')


class ListingAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
  resource_class = ListingResource
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'title')
  list_filter = ('realtor',)
  list_editable = ('is_published',)
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)