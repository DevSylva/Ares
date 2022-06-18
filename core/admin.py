from django.contrib import admin
from .models import *
# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", "amount")
    list_filter = ("user", "date_created",)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "status", "type")
    list_filter = ("user", "type", "status", "plan", "date_created")

class WalletAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    list_filter = ("name",)

class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "pricing")


admin.site.register(Plan, PlanAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Payment, PaymentAdmin)