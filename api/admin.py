from django.contrib import admin
from .models import work

class CustAdminPanel(admin.ModelAdmin):
    # using custom display for admin panel
    list_display = ('title', 'completed')

admin.site.register(work, CustAdminPanel)
