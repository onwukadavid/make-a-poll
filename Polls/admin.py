from django.contrib import admin
from Polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    min_num = 2
    max_num = 4

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'question', 'pub_date', 'updated_at', 'status', 'slug', 'thumbnail', 'user']

    fieldsets = [
        ('Poll information', {"fields":['title', 'description', 'status', 'slug', 'question', 'user']}),
        ('Date information', {"fields":['pub_date', 'updated_at']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('title', 'description', 'status', 'user', 'deleted_at')
    list_filter = ['status', 'user', 'deleted_at']
    search_fields = ['title', 'description']
    

admin.site.register(Question, QuestionAdmin)