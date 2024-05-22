# Register your models here.
#polls/admin.py

#diop
#Ibrahima1
from django.contrib import admin
from .models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
admin.site.register(Question, QuestionAdmin)

# class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
        # (None,{'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date']}),
    # ]
# admin.site.register(Question, QuestionAdmin)


# class ChoiceInline(admin.StackedInline):
    # model = Choice
    # extra = 3


# class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
        # (None,{'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    # inlines = [ChoiceInline]
    # list_display = ('question_text', 'pub_date', 'was_published_recently')

# admin.site.register(Question, QuestionAdmin)


###--------------------------------------------------------------
# from import_export.admin import ImportExportModelAdmin
# from django.contrib import admin
# from .models import Employee

# @admin.register(Employee)
# class EmployeeAdmin(ImportExportModelAdmin):
    # pass