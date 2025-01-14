from django.contrib import admin
from Polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    min_num = 2
    max_num = 4

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'question', 'pub_date', 'updated_at', 'status', 'slug', 'thumbnail', 'author']

    fieldsets = [
        ('Poll information', {"fields":['title', 'description', 'status', 'slug', 'question', 'author']}),
        ('Date information', {"fields":['pub_date', 'updated_at']}),
    ]

    inlines = [ChoiceInline]
    readonly_fields = ['slug']
    list_display = ('title', 'description', 'status', 'author', 'deleted_at')
    list_filter = ['status', 'author', 'deleted_at']
    search_fields = ['title', 'description']
    

admin.site.register(Question, QuestionAdmin)