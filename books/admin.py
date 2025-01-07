from django.contrib import admin
from .models import Author,Category,Publisher,Review,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','bio','birth_day','death_date','web_site','web_site','author_avatar']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name','address','web_site']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','book','comment','rate']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author','slug','publisher','price','last_price','cover_pic','ebook','audio_book','description','stock']
    list_filter = ['category']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Review,ReviewAdmin)
