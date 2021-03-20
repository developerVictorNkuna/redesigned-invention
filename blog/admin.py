from django.contrib import admin
#import models here
import blog 
from blog.models  import Post , Comment ,Category
# Register your models here.

class  PostAdmin(admin.ModelAdmin):
    list_display = ("title","publish_status","created_on")
    list_filter = ["publish_status"]
    search_fields = ["title","content"]
    prepopulated_fields ={'topic_category':["title"]}
admin.site.register(Post,PostAdmin )



# class Catergory(admin.ModelAdmin):
#     topic_category =["title"]
# admin.site.register(Catergory)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Category)