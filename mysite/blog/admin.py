from django.contrib import admin
from mysite.blog.models import Author, Article

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('date',)
    date_hierarchy = 'date'
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
