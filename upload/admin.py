from django.contrib import admin
from django.db import connection
from .models import UploadCriminal

# Register your models here.

def verify_upload(modeladmin, request, queryset):
    for criminal in queryset:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO %s (name, age, physical_description, date, state_id, city_id, crime_type_id, arresting_agency, photo, rating, status, fir_no, fir_photo) SELECT name, age, physical_description, date, state_id, city_id, crime_type_id, arresting_agency, photo, '0', status, fir_no, fir_photo FROM %s WHERE criminal_id = %s" % ("criminals_verifiedcriminal", "upload_uploadCriminal", int(criminal.criminal_id)))

verify_upload.short_description = "Add to criminal DB"

class UploadCriminalAdmin(admin.ModelAdmin):
    actions = [verify_upload]

admin.site.register(UploadCriminal, UploadCriminalAdmin)