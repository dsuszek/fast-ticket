from django.contrib import admin
from ticket import models

@admin.register(models.Category)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
