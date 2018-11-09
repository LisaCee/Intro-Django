from django.contrib import admin
from .models import Media, Book, Music, Movie, Reviewer
# Register your models here.
class MediaAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')
	list_dispay = ('title', 'author')

admin.site.register(Media, MediaAdmin)
admin.site.register(Book)
admin.site.register(Music)
admin.site.register(Movie)
admin.site.register(Reviewer)




