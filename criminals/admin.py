from django.contrib import admin
from .models import VerifiedCriminal, States, Cities

# Register your models here.
admin.site.register(VerifiedCriminal)
admin.site.register(States)
admin.site.register(Cities)