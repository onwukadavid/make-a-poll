from django.contrib import admin
from Polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'question', 'pub_date', 'updated_at', 'status', 'slug', 'thumbnail']

admin.site.register(Question, QuestionAdmin)