from django.contrib import admin

# Register your models here.
from pharmaapp.models import DrugReview, PharmaSales

admin.site.register(DrugReview)
admin.site.register(PharmaSales)