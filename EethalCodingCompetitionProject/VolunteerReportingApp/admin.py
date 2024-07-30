from django.contrib import admin

# Register your models here.
from .models import Team, Student, VolunteerLog
admin.site.register(Team)
admin.site.register(Student)
admin.site.register(VolunteerLog)
