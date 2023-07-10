from django.contrib import admin
from blog.models import BlogPost, Author

class BlogAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'description', 'date', 'author')
    list_filter = ('date')
    list_search =('title', 'description')
    fieldsets = (
        ('Basic Information', {
            "fields": ('title', 'description')
        }),
        ('More Information', {
            'classes': ('collapse', 'wide')
        })
    )

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Author)