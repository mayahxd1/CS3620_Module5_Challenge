from django.contrib import admin
from .models import Registration, EventSession, DietSection


# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("user_first_name", "user_last_name", "user_email", "user_phone", "event_session")
    list_filter = ("event_session",)


class EventSessionAdmin(admin.ModelAdmin):
    list_display = ("event_name", "event_description")


class DietSectionAdmin(admin.ModelAdmin):
    list_display = ("diet_description", "registration")
    list_filter = ("registration__user_first_name", "registration__user_last_name", "registration__event_session")


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(EventSession, EventSessionAdmin)
admin.site.register(DietSection, DietSectionAdmin)
