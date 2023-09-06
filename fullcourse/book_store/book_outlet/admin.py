from django.contrib import admin

# Register your models here.
from .models import Book, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug', )
    prepopulated_fields = {
        'slug': ('title', )
    }

    list_filter = ('title', 'author', 'rating')
    list_display = ('id', 'title', 'author', 'rating')


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)