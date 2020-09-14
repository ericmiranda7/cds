from django.contrib import admin
from .models import UploadCriminal
from criminals.models import Criminal
from django.db import connection

# Register your models here.

def verify_upload(modeladmin, request, queryset):
    for criminal in queryset:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO %s (name, age, physical_description, date, state_id, city_id, crime_type, arresting_agency, photo, rating, status) SELECT name, age, physical_description, date, state_id, city_id, crime_type, arresting_agency, photo, '0', status FROM %s WHERE id = %s" % ("criminals_criminal", "upload_uploadCriminal", int(criminal.id)))

verify_upload.short_description = "Add to criminal DB"

class UploadCriminalAdmin(admin.ModelAdmin):
    actions = [verify_upload]

admin.site.register(UploadCriminal, UploadCriminalAdmin)