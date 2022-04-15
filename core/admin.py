from django.contrib import admin
from .models import (
    Pupil,
    Teacher,
    Staff,
    Class,
)
# Register your models here.


class PupilAdmin(admin.ModelAdmin):
    list_filter = ('sex',)

class TeacherAdmin(admin.ModelAdmin):
    list_filter = ('sex',)

class StaffAdmin(admin.ModelAdmin):
    list_filter = ('sex', 'role')


admin.site.register(Pupil, PupilAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Staff, StaffAdmin)

admin.site.register(Class)
