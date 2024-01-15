from django.contrib import admin
from Polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'question', 'pub_date', 'updated_date', 'status', 'slug', 'thumbnail']

admin.site.register(Question, QuestionAdmin)