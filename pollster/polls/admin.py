from dataclasses import fields
from django.contrib import admin
from .models import Question, Choices

# Register your models here.

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to Pollster admin area"

class ChoiceInLine(admin.TabularInline):
    model = Choices
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields' : ['question_text']}),
     ('Date Information',{'fields' : ['pub_date'], 'classes' : ['collapse']}), ]

    inlines = [ChoiceInLine]

# admin.site.register(Question)
# admin.site.register(Choices)

admin.site.register(Question, QuestionAdmin)
