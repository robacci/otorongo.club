from django.contrib import admin

from votes.models import Person


class PersonAdmin(admin.ModelAdmin):
    model = Person


admin.site.register(Person, PersonAdmin)
