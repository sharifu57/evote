from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .models import User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description')

admin.site.register(Category, CategoryAdmin)


class NominationAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'index')

admin.site.register(Nomination, NominationAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display = ('category', 'nomination', 'created_at')

admin.site.register(Vote, VoteAdmin)

