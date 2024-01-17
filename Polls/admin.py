from django.contrib import admin
from Polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    min_num = 2
    max_num = 4

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['title', 'description', 'question', 'pub_date', 'updated_at', 'status', 'slug', 'thumbnail', 'user']

    fieldsets = [
        ('Poll information', {"fields":['title', 'description', 'status', 'slug', 'question']}),
        ('Date information', {"fields":['pub_date', 'updated_at']}),
    ]

    inlines = [ChoiceInline]

    

admin.site.register(Question, QuestionAdmin)