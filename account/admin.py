from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "account_balance", "alaye")
    list_filter = ("username", "email", "alaye")

admin.site.register(User, UserAdmin)
