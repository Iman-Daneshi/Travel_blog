from django.contrib import admin
from website.models import Contact, NewsLetter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date', )
    list_filter  = ('email',)
    search_fields = ['name', 'message']

class NewsLetterAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('email', 'created_date', )
    list_filter  = ('email',)
    search_fields = ['email']


admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(Contact, ContactAdmin)
