from django.contrib import admin

from url_shorter_app.models import RedirectModel


@admin.register(RedirectModel)
class RedirectModelAdmin(admin.ModelAdmin):
    readonly_fields = ('short_path', 'redirect_counter')
    list_display = ('target_url', 'short_path', 'redirect_counter')
    search_fields = ('target_url', )
