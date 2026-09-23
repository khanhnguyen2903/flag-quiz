from django.contrib import admin
from .models import Flag


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = (
        "country_name",
        "capital_name",
        "continent",
        "url_flag",
    )

    list_filter = (
        "continent",
    )

    search_fields = (
        "country_name",
        "capital_name",
    )
