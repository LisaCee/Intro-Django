from django.contrib import admin
from .models import Books, PersonalBooks
# Register your models here.
class BookAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

admin.site.register(Books)
admin.site.register(PersonalBooks)


