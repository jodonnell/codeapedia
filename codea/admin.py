from codea.models import Tags, Quotes
from django.contrib import admin

class QuotesAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'quote')

admin.site.register(Tags)
admin.site.register(Quotes, QuotesAdmin)
