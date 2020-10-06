from django.contrib import admin

# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    pass