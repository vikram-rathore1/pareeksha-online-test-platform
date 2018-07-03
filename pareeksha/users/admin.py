# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('other info', {'fields': ('role',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'role', 'is_superuser'),
        }),
    )

    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = (
        'email',
        'first_name',
        'last_name',
        'role',
        'is_superuser',
    )

    list_filter = (
        'is_superuser',
    )

    search_fields = (
        'first_name',
        'last_name',
        'role',
        'email'
    )

    ordering = (
        'email',
    )

    filter_horizontal = ()

admin.site.register(User, CustomUserAdmin)
