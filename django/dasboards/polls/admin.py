from django.contrib import admin
from .models import Upload
from .models import Question,Choice
#from import_export.admin import ImportExportModelAdmin

# Register your models here.
# Make the poll app modifiable in the admin
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Upload)
