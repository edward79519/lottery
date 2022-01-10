from django.contrib import admin
from .models import Employee, Prize, Title, Department, AwardList


# Register your models here.
admin.site.register(Employee)
admin.site.register(Prize)
admin.site.register(Title)
admin.site.register(Department)
admin.site.register(AwardList)