from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Stockinfo, Stock_list

@admin.register(Stock_list)
class MemberAdmin(ImportExportModelAdmin):
    list_display = ("corpName", "corpCode", "corpCategory")
    pass
# @admin.register(Member)
# class MemberAdmin(ImportExportModelAdmin):
#     list_display = ("firstname", "lastname", "email", "birth_date")
#     pass
admin.site.register(Stockinfo)
